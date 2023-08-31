import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Waiting client conection...")
    conn, addr = server_socket.accept()
    print(f"Connected with {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.send(data)
    conn.close()

if __name__ == "__main__":
    main()
