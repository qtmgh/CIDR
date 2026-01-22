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

