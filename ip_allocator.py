print("IP Allocator Module Loaded")

def compute_network_details(base_ip, cidr):
    parts = base_ip.split(".")
    network_prefix = ".".join(parts[:3])
    base_host = int(parts[3])

    host_bits = 32 - cidr
    total_hosts = 2 ** host_bits

    network_host = (base_host // total_hosts) * total_hosts
    broadcast_host = network_host + total_hosts - 1

    return network_host, broadcast_host



NETWORK_BASE = "192.168.10"
BASE_IP = "192.168.10.0"
CIDR = 26
RESERVED_RANGES= [
    (1, 29, "Infrastructure"),
]

network_host, broadcast_host = compute_network_details(BASE_IP, CIDR)

NETWORK_ADDRESS = network_host
BROADCAST_ADDRESS = broadcast_host

RESERVED_HOSTS = {
    1: "Router",
    10: "File Server",
    20: "Printer A", 
    21: "Printer B",
}

USER_START = 60
USER_END = BROADCAST_ADDRESS - 1



def make_ip(host_number):
    return NETWORK_BASE + "." + str(host_number)

def in_reserved_range(host):
    for start, end, label in RESERVED_RANGES:
        if start <= host <= end:
            return label
    return None

def is_valid_host(host):
    if host == NETWORK_ADDRESS:
        return False
    if host == BROADCAST_ADDRESS:
        return False
    if host in RESERVED_HOSTS:
        return False
    
    label = in_reserved_range(host)
    if label is not None:
        return False
    
    if host < USER_START:
        return False
    
    return True

def validate_policy():
    if USER_START <= NETWORK_ADDRESS:
        raise RuntimeError("USER_START is at or below the network address.")
    
    if USER_START >= BROADCAST_ADDRESS:
        raise RuntimeError("USER_START is at or above the broadcast address.")
    
    # USER_START must not sit inside a reserved range
    label = in_reserved_range(USER_START)
    if label is not None:
        raise RuntimeError(f"USER_START falls within reserved range: " + label)
    
    # Make sure reserved ranges do not include network or broadcast
    for start, end, label in RESERVED_RANGES:
        if start <= NETWORK_ADDRESS <= end:
            raise RuntimeError("Reserved range includes network address: " + label)
        if start <= BROADCAST_ADDRESS <= end:
            raise RuntimeError("Reserved range includes broadcast address: " + label)


def allocate_users(count):
    validate_policy()
    allocated = []
    current = USER_START

    while len(allocated) < count and current <= USER_END:
        if is_valid_host(current):
            allocated.append(make_ip(current))
            current += 1
    if len(allocated) < count:
        raise Exception("Not enough available IP addresses to allocate.")
    
    return allocated




def main():
    users_needed = 18
    users_ips = allocate_users(users_needed)

    print("Allocated user IPs:")
    for ip in users_ips:
        print(ip)
    
print("Network address:", make_ip(NETWORK_ADDRESS))
print("Broadcast address:", make_ip(BROADCAST_ADDRESS))
print("Usable range:", make_ip(NETWORK_ADDRESS + 1), "to", make_ip(BROADCAST_ADDRESS - 1))


if __name__ == "__main__":
    main()
