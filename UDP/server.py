import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('localhost', 8080))
    print("Using UDP - Waiting client conection...")
    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received: {data.decode()} from {addr}")
        udp_socket.sendto(data, addr)

if __name__ == "__main__":
    main()
