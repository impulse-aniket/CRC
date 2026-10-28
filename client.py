import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5001))

print("Connected to server.")

while True:
    message = input("Client: ")
    client.send(message.encode())

    if message.lower() == "bye":
        break

    reply = client.recv(1024).decode()

    if not reply:
        break

    print("Server:", reply)

    if reply.lower() == "bye":
        break

client.close()
