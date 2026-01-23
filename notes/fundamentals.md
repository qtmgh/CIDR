# Fundamentals

## Core Definitions

### IPv4 Address
- 32-bit number written as four octets.
- Example: 192.168.10.50
- Identifies a single device on a network.

### Bit 
- Smallest unit of data. 
- Value is 0 or 1.
- IPv4 uses 32 bits total. (4 octets, 8 bits each octet, 8 x 4 = 32)

### Network Bits 
- Fixed portion of the IP. 
- Identifies the subnet.
- Same for every device in that subnet.

### Host Bits 
- Variable portion of the IP.
- Identifies individual devices.
- Number of host bits controls how many devices exist.


## CIDR 

### What CIDR Means
- CIDR is Classless Inter-Domain Routing.
- Written as a slash followed by a number. (/26)

### What CIDR Represents
- The number of network bits.
- CIDR = network bits. 
- CIDR = 32 - host bits.

### Key Formula
- Usable hosts = (2 ^ host bits) - 2
- We subtract 2 for network address and broadcast address.


## Network and Broadcast Addresses

### Network Address
- All host bits set to 0.
- Identifies the subnet itself.
- Not assigned to a device.

### Broadcast Address
- All host bits set to 1. 
- Used to reach all devices on the subnet.
- Not assigned to a device as well.

### Host Range 
- All of the addresses between the network and broadcast.
- These are usable device IPs.


## Subnet Sizing Logic

### How to Choose CIDR
1. Determine how many devices you need.
2. Find smallest power of two that supports them.
3. That power determines host bits.
4. CIDR = 32 - host bits.

### Example
- Need 40 devices.
- 2^6 = 64 addresses.
- 64-2 = 62 usable hosts.
- Host bits = 6. 
- CIDR = 26. 

## Real-World IP Addressing Conventions

### Infrastructure Addresses
- Assigned low IPs. 
- Examples:
    + Router or gateway at .1
    + Servers around .10
    + Printers around .20

### User Devices
- Assigned higher IPs.
- Easier to manage and scale.
- Keeps roles predictable.

### Why Consistency Matters
- Faster troubleshooting.
- Clear documentation. 
- Lower risk of IP conflicts.
- Easier onboarding for new admins. 

## Mental Models
- CIDR locks bits from the left. 
- Host bits create device addresses.
- Network address is lowest.
- Broadcast address is highest. 
- Subnet design is about intention, not convenience.

