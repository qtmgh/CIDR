# cli.py
# Purpose: Command-line interface for the IP allocator engine

import argparse
import ip_allocator


def build_parser():
    # This defines what options the CLI accepts
    p = argparse.ArgumentParser(
        prog="ipalloc",
        description="Allocate user IPs from a subnet with reserved ranges."
    )

    # These flags become args.base_ip, args.cidr, args.users, args.user_start
    p.add_argument("--base-ip", required=True, help="Example: 192.168.10.0")
    p.add_argument("--cidr", required=True, type=int, help="Example: 26")
    p.add_argument("--users", required=True, type=int, help="How many user IPs to allocate")
    p.add_argument("--user-start", default=30, type=int, help="First host number for users (policy)")

    return p


def main():
    # Parse what the user typed into 'args'
    parser = build_parser()
    args = parser.parse_args()

    # Office policy: specific reserved devices
    reserved_hosts = {
        1: "Router",
        10: "File Server",
        20: "Printer A",
        21: "Printer B",
    }

    # Office policy: reserve a whole infrastructure zone
    reserved_ranges = [
        (1, 29, "Infrastructure"),
    ]

    # Call the allocator engine with the user's inputs
    result = ip_allocator.allocate_from_inputs(
        base_ip=args.base_ip,
        cidr=args.cidr,
        users_needed=args.users,
        user_start=args.user_start,
        reserved_hosts=reserved_hosts,
        reserved_ranges=reserved_ranges,
    )

    # Print results
    print("\nSubnet summary:")
    print("Network:", result["network"])
    print("Broadcast:", result["broadcast"])
    print("Usable:", result["usable_start"], "to", result["usable_end"])

    print("\nAllocated user IPs:")
    for ip in result["allocated"]:
        print(ip)


# This ensures main() runs only when you execute cli.py directly
if __name__ == "__main__":
    main()
