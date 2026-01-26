def allocate_from_inputs(base_ip, cidr, users_needed, user_start, reserved_hosts, reserved_ranges):
    parts = base_ip.split(".")
    prefix = ".".join(parts[:3])
    base_host = int(parts[3])

    host_bits = 32 - cidr
    block_size = 2 ** host_bits

    network_host = (base_host // block_size) * block_size
    broadcast_host = network_host + block_size - 1

    def make_ip(h):
        return prefix + "." + str(h)

    def in_reserved_range(h):
        for start, end, label in reserved_ranges:
            if start <= h <= end:
                return label
        return None

    # Policy validation (fail fast)
    label = in_reserved_range(user_start)
    if label is not None:
        raise RuntimeError("USER_START falls within reserved range: " + label)

    if user_start <= network_host or user_start >= broadcast_host:
        raise RuntimeError("USER_START must be inside usable host range")

    # Allocate
    allocated = []
    h = user_start
    last_host = broadcast_host - 1

    while len(allocated) < users_needed and h <= last_host:
        if h == network_host or h == broadcast_host:
            h += 1
            continue

        if h in reserved_hosts:
            h += 1
            continue

        if in_reserved_range(h) is not None:
            h += 1
            continue

        allocated.append(make_ip(h))
        h += 1

    if len(allocated) < users_needed:
        raise RuntimeError("Not enough IP addresses available")

    return {
        "network": make_ip(network_host),
        "broadcast": make_ip(broadcast_host),
        "usable_start": make_ip(network_host + 1),
        "usable_end": make_ip(broadcast_host - 1),
        "allocated": allocated,
    }
