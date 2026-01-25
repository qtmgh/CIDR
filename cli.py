import argparse
import ip_allocator

def build_parser():
    p = argparse.ArgumentParser(
        prog = "ipalloc",
        description= "Allocate user IPs from a subnet with reserved ranges."    
    )
    p.add_argument("--base-ip", required=True, help="192.168.10.0")
    p.add_argument("--cidr", required=True, type=int, help= "Example: 26")
    p.add_argument("--users", required=True, type=int, help= "Number of user IPs t0 allocate")

    p.add_argument("--user-start", default=30, type=int, help="First host number for users, default is 30")

    return p

def main():
    parser = build_parser()
    args = parser.parse_args()

    print("Inputs:")
    print("Base IP:", args.base_ip)
    print("CIDR: /" + str(args.cidr))
    print("Users:", args.users)
    print("User start:", args.user_start)



if __name__ == "__main__":
    main()
