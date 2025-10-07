import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12346)  # Change to server IP in LAN
print("UDP Client started.")

while True:
    msg = input("You: ")
    client_socket.sendto(msg.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print(f"Server: {data.decode()}")