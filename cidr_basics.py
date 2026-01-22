def octet_to_binary(n):
    bits = []
    values = [128, 64, 32, 16, 8, 4, 2, 1]

    for v in values:
        if n >= v:
            bits.append("1")
            n -= v
        else:
            bits.append("0")

    return "".join(bits)

print(octet_to_binary(192))
print(octet_to_binary(168))
print(octet_to_binary(1))
print(octet_to_binary(50))



def ip_to_bits(ip):
    octets = ip.split(".")
    bits = ""

    for o in octets:
        bits += octet_to_binary(int(o))
    
    return bits  # 32 chars, no spacing

def format_bits(bits):
    return bits[0:8] + " " + bits[8:16] + " " + bits[16:24] + " " + bits[24:32]

def bits_to_ip(bits32):
    octets = []
    for i in range(0, 32, 8):
        chunk = bits32[i:i+8]
        octets.append(str(int(chunk, 2)))
    return ".".join(octets)


def apply_cidr(bits32, cidr):
    network_bits = bits32[:cidr]
    host_bits = bits32[cidr:]
    return network_bits, host_bits

def network_address(bits32, cidr):
    net = bits32[:cidr]
    host_len = 32 - cidr
    return net + ("0" * host_len)

def broadcast_address(bits32, cidr):
    net = bits32[:cidr]
    host_len = 32 - cidr
    return net + ("1" * host_len)


ip = "192.168.1.50"
cidr = 24


bits32 = ip_to_bits(ip)
net_bits, host_bits = apply_cidr(bits32, cidr)

net_addr_bits = network_address(bits32, cidr)
bcast_bits = broadcast_address(bits32, cidr)

print("IP:", ip)
print("CIDR: /" + str(cidr))
print("Full 32 bits:", format_bits(bits32))
print("Network bits:", net_bits)
print("Host bits:", host_bits)

print("Network address bits:", format_bits(net_addr_bits))
print("Network address:", bits_to_ip(net_addr_bits))

print("Broadcast bits:", format_bits(bcast_bits))
print("Broadcast address:", bits_to_ip(bcast_bits))
