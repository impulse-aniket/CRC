import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 5001))
    n = input("Enter an integer: ")
    client.sendall(n.encode())

    result = client.recv(1024).decode()
    print("Factorial:", result)

finally:
    client.close()
