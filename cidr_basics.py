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


def apply_cidr(bits32, cidr):
    network_bits = bits32[:cidr]
    host_bits = bits32[cidr:]
    return network_bits, host_bits

bits32 = ip_to_bits("192.168.1.50")
network, host = apply_cidr(bits32, 24)
print("Full 32 bits:", format_bits(bits32))
print("Network bits:", network)
print("Host bits:", host)
print("Network bit count:", len(network))
print("Host bit count:", len(host))
