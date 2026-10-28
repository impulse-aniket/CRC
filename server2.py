import socket
import math

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

try:
    data = conn.recv(1024).decode().strip()
    n = int(data)

    if n < 0:
        result = "Factorial is not defined for negative integers"
    else:
        result = str(math.factorial(n))

    conn.sendall(result.encode())
    print("Factorial sent to client:", result)

except ValueError:
    conn.sendall(b"Invalid input. Please send an integer.")

finally:
    conn.close()
    server.close()
