NETWORK_BASE = "192.168.10"
BASE_IP = "192.168.10.0"
CIDR = 25
RESERVED_RANGES = [
    (1, 29, "Infrastructure"),
]

RESERVED_HOSTS = {
    1: "Router",
    10: "File Server",
    20: "Printer A", 
    21: "Printer B",
}

USER_START = 30


def compute_network_details(base_ip, cidr):
    parts = base_ip.split(".")
    network_prefix = ".".join(parts[:3])
    base_host = int(parts[3])

    host_bits = 32 - cidr
    total_hosts = 2 ** host_bits

    network_host = (base_host // total_hosts) * total_hosts
    broadcast_host = network_host + total_hosts - 1

    return network_host, broadcast_host


def get_network_bounds():
    network_host, broadcast_host = compute_network_details(BASE_IP, CIDR)
    return network_host, broadcast_host


def get_user_end():
    _, broadcast_host = get_network_bounds()
    return broadcast_host - 1



def make_ip(host_number):
    return NETWORK_BASE + "." + str(host_number)

def in_reserved_range(host):
    for start, end, label in RESERVED_RANGES:
        if start <= host <= end:
            return label
    return None

def is_valid_host(host):
    network_address, broadcast_address = get_network_bounds()
    user_end = get_user_end()

    if host == network_address:
        return False
    if host == broadcast_address:
        return False
    if host in RESERVED_HOSTS:
        return False
    
    label = in_reserved_range(host)
    if label is not None:
        return False
    
    if host < USER_START:
        return False
    if host > user_end:
        return False
    
    return True

def validate_policy():
    network_address, broadcast_address = get_network_bounds()
    if USER_START <= network_address:
        raise RuntimeError("USER_START is at or below the network address.")
    
    if USER_START >= broadcast_address:
        raise RuntimeError("USER_START is at or above the broadcast address.")
    
    # USER_START must not sit inside a reserved range
    label = in_reserved_range(USER_START)
    if label is not None:
        raise RuntimeError(f"USER_START falls within reserved range: " + label)
    
    # Make sure reserved ranges do not include network or broadcast
    for start, end, label in RESERVED_RANGES:
        if start <= network_address <= end:
            raise RuntimeError("Reserved range includes network address: " + label)
        if start <= broadcast_address <= end:
            raise RuntimeError("Reserved range includes broadcast address: " + label)


def allocate_users(count):
    validate_policy()
    allocated = []
    current = USER_START
    user_end = get_user_end()

    while len(allocated) < count and current <= user_end:
        if is_valid_host(current):
            allocated.append(make_ip(current))
            current += 1
    if len(allocated) < count:
        raise Exception("Not enough available IP addresses to allocate.")
    
    return allocated




def main():
    users_needed = 18
    users_ips = allocate_users(users_needed)
    network_address, broadcast_address = get_network_bounds()

    print("Allocated user IPs:")
    for ip in users_ips:
        print(ip)
    
    print("Network address:", make_ip(network_address))
    print("Broadcast address:", make_ip(broadcast_address))
    print("Usable range:", make_ip(network_address + 1), "to", make_ip(broadcast_address - 1))


if __name__ == "__main__":
    main()
