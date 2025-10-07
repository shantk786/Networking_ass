import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 12346))
print("UDP Server listening on port 12346...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Client: {data.decode()}")
    reply = input("You: ")
    server_socket.sendto(reply.encode(), addr)