import socket


try:
    from colorama import init, Fore
    init()
except ImportError:
    print("Install colorama with 'pip install colorama' for colored output")
    Fore = type('', (), {'GREEN':'', 'RED':'', 'RESET':''})()  # fallback

# User input
host = input("Enter host (e.g., 127.0.0.1): ")
start_port = int(input("Enter start port (e.g., 20): "))
end_port = int(input("Enter end port (e.g., 1024): "))

print(f"\nScanning {host} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(Fore.GREEN + f"Port {port} is OPEN" + Fore.RESET)
    else:
        print(Fore.RED + f"Port {port} is closed" + Fore.RESET)
    sock.close()

print("\nScanning completed!")

