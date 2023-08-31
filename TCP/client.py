import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    client_socket.sendall(b"Hello Server TCP!")
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    client_socket.close()

if __name__ == "__main__":
    main()
