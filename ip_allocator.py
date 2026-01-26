def allocate_from_inputs(base_ip, cidr, users_needed, user_start, reserved_hosts, reserved_ranges):
    # Split the base IP into octets so we can derive the network prefix and host number.
    parts = base_ip.split(".")
    # Keep the first three octets as the network prefix (e.g., "192.168.10").
    prefix = ".".join(parts[:3])
    # Parse the last octet as an integer host value.
    base_host = int(parts[3])

    # Calculate how many host bits remain for the given CIDR.
    host_bits = 32 - cidr
    # Compute the subnet block size (number of addresses in the subnet).
    block_size = 2 ** host_bits

    # Find the network address host number by rounding down to the subnet boundary.
    network_host = (base_host // block_size) * block_size
    # The broadcast host number is the last address in the subnet.
    broadcast_host = network_host + block_size - 1

    def make_ip(h):
        # Build a full dotted IP address from the prefix and host number.
        return prefix + "." + str(h)

    def in_reserved_range(h):
        # Check if a host number is inside any reserved range.
        for start, end, label in reserved_ranges:
            if start <= h <= end:
                return label
        return None

    # Policy validation (fail fast)
    # Ensure the user-start host is not inside a reserved range.
    label = in_reserved_range(user_start)
    if label is not None:
        raise RuntimeError("USER_START falls within reserved range: " + label)

    # Ensure the user-start host is within the usable subnet range.
    if user_start <= network_host or user_start >= broadcast_host:
        raise RuntimeError("USER_START must be inside usable host range")

    # Allocate
    # Prepare the allocation list and start from the requested first user host.
    allocated = []
    h = user_start
    # The last usable host is one before the broadcast address.
    last_host = broadcast_host - 1

    # Walk through hosts until we allocate the requested number or run out.
    while len(allocated) < users_needed and h <= last_host:
        # Skip the network and broadcast addresses explicitly.
        if h == network_host or h == broadcast_host:
            h += 1
            continue

        # Skip explicitly reserved single hosts.
        if h in reserved_hosts:
            h += 1
            continue

        # Skip hosts that fall into any reserved range.
        if in_reserved_range(h) is not None:
            h += 1
            continue

        # This host is usable; allocate it.
        allocated.append(make_ip(h))
        h += 1

    # If we couldn't allocate enough addresses, fail with an error.
    if len(allocated) < users_needed:
        raise RuntimeError("Not enough IP addresses available")

    # Return a summary of the subnet and the allocated IPs.
    return {
        "network": make_ip(network_host),
        "broadcast": make_ip(broadcast_host),
        "usable_start": make_ip(network_host + 1),
        "usable_end": make_ip(broadcast_host - 1),
        "allocated": allocated,
    }
