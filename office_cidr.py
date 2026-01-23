""" Example: Let's say we have 40 devices
    We need to find out how many host bits we need... we came to a conclusion of 6 host bits because 2^6 supports 64 devices.
    Now we need to find the CIDR (the number of network bits) -->  CIDR = 32 - host bits
    CIDR = /26 """

# The reason CIDR exists is for allocating, scaling, and segmenting space... if everyone sized networks the same, CIDR would be pointless.

# The amount of usable hosts is the amount of address combinations each host bit has subtracted by 2 because there are two special combinations... the network address (000000) and the broadcast address (111111) which are NOT devices, they are reserved patterns.

def cidr_for_hosts(needed_hosts):
    for host_bits in range(1,33):
        total = 2 ** host_bits
        usable = total - 2
        if usable >= needed_hosts:
            return host_bits, 32 - host_bits
        
needed = 40
host_bits, cidr = cidr_for_hosts(needed)

print("Needed hosts:", needed)
print("Host bits:", host_bits)
print("CIDR: /", str(cidr))