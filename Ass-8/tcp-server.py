import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))  # Listen on all interfaces, port 12345
server_socket.listen(1)
print(" TCP Server listening on port 12345...")

conn, addr = server_socket.accept()
print(f"🔗Connected to {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()