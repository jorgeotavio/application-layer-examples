import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(b"Hello server UDP!", ('localhost', 8080))
    data, addr = udp_socket.recvfrom(1024)
    print(f"Received: {data.decode()} from {addr}")

if __name__ == "__main__":
    main()
