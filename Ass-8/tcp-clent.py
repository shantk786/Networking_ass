import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))  # Change to server IP in LAN
print("Connected to server.")

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    reply = client_socket.recv(1024).decode()
    print(f"Server: {reply}")

client_socket.close()