import argparse
import ip_allocator


def build_parser():
    p = argparse.ArgumentParser(
        prog="ipalloc",
        description="Allocate user IPs from a subnet with reserved ranges."
    )

    p.add_argument("--base-ip", required=True)
    p.add_argument("--cidr", required=True, type=int)
    p.add_argument("--users", required=True, type=int)
    p.add_argument("--user-start", default=30, type=int)

    return p


def main():
    parser = build_parser()
    args = parser.parse_args()

    reserved_hosts = {
        1: "Router",
        10: "File Server",
        20: "Printer A",
        21: "Printer B",
    }

    reserved_ranges = [
        (1, 29, "Infrastructure"),
    ]

    result = ip_allocator.allocate_from_inputs(
        base_ip=args.base_ip,
        cidr=args.cidr,
        users_needed=args.users,
        user_start=args.user_start,
        reserved_hosts=reserved_hosts,
        reserved_ranges=reserved_ranges,
    )

    print("\nSubnet summary:")
    print("Network:", result["network"])
    print("Broadcast:", result["broadcast"])
    print("Usable:", result["usable_start"], "to", result["usable_end"])

    print("\nAllocated user IPs:")
    for ip in result["allocated"]:
        print(ip)


if __name__ == "__main__":
    main()
