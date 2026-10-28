import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5001))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    if message.lower() == "bye":
        print("Client ended the chat.")
        break

    print("Client:", message)

    reply = input("Server: ")
    conn.send(reply.encode())

    if reply.lower() == "bye":
        break

conn.close()
server.close()
