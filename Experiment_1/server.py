import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5000

server_socket.bind((host, port))

server_socket.listen(1)

print("Server is waiting for a connection...")

client_socket, client_address = server_socket.accept()

print("Connected to:", client_address)

message = client_socket.recv(1024).decode()

print("Message received from client:", message)

response = "Message received successfully!"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()
