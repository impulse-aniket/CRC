# Hamming Code: Error Detection and Correction (Even Parity)

def calculate_parity(code, parity_pos):
    count = 0

    for i in range(1, len(code)):
        if i & parity_pos:
            if code[i] == '1':
                count += 1

    return count % 2


# Sender Side
data = input("Enter data bits: ")

if not data or any(bit not in '01' for bit in data):
    print("Invalid input! Enter only 0s and 1s.")
    exit()

m = len(data)

# Calculate number of parity bits
r = 0
while 2 ** r < m + r + 1:
    r += 1

n = m + r

# Initialize code array (positions start at 1)
code = ['0'] * (n + 1)

# Insert data bits into non-parity positions
j = 0
for i in range(1, n + 1):
    if i & (i - 1):  # Not a power of 2
        code[i] = data[j]
        j += 1

# Calculate even parity bits
for i in range(r):
    pos = 2 ** i
    code[pos] = str(calculate_parity(code, pos))

# Display generated Hamming code
generated = ''.join(code[i] for i in range(n, 0, -1))
print("Generated Hamming Code:", generated)


# Receiver Side
received_input = input("Enter received code: ")

if len(received_input) != n or any(bit not in '01' for bit in received_input):
    print("Invalid received code!")
    exit()

received = ['0'] + list(received_input[::-1])

# Detect error
error = 0

for i in range(r):
    pos = 2 ** i
    if calculate_parity(received, pos):
        error += pos

# Display and correct error
if error == 0:
    print("No Error Detected")
else:
    print("Error at position:", error)

    if error <= n:
        received[error] = '1' if received[error] == '0' else '0'

        corrected = ''.join(received[i] for i in range(n, 0, -1))
        print("Corrected Code:", corrected)
    else:
        print("Error position is outside the received code.")