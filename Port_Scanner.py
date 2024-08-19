import socket


# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


# Function to scan common ports
def scan_common_ports(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 587, 3389]
    print("Scanning common ports...")
    for port in common_ports:
        scan_port(ip, port)


# Function to scan all ports
def scan_all_ports(ip):
    print("Scanning all ports...")
    for port in range(1, 65536):
        scan_port(ip, port)


# Function to scan custom ports
def scan_custom_ports(ip, ports):
    print("Scanning custom ports...")
    for port in ports:
        scan_port(ip, port)


# Main function
def main():
    ip = input("Enter the IP address to scan: ")

    print("Select scan option:")
    print("1. Common ports")
    print("2. All ports")
    print("3. Custom ports")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        scan_common_ports(ip)
    elif choice == '2':
        scan_all_ports(ip)
    elif choice == '3':
        custom_ports = input("Enter custom ports separated by commas: ")
        custom_ports = list(map(int, custom_ports.split(',')))
        scan_custom_ports(ip, custom_ports)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
