def xor(a, b):
    result = ""
    for i in range(len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result


def crc(data, divisor):
    n = len(divisor)
    tmp = data[:n]

    for i in range(n, len(data)):
        if tmp[0] == '1':
            tmp = xor(tmp, divisor)[1:] + data[i]
        else:
            tmp = xor(tmp, '0' * n)[1:] + data[i]

    if tmp[0] == '1':
        tmp = xor(tmp, divisor)[1:]
    else:
        tmp = xor(tmp, '0' * n)[1:]

    return tmp


data = input("Enter data: ")
divisor = input("Enter Generator Polynomial: ")

appended_data = data + '0' * (len(divisor) - 1)
remainder = crc(appended_data, divisor)
codeword = data + remainder

print("CRC Remainder:", remainder)
print("Transmitted Codeword:", codeword)

received = input("Enter received codeword: ")
check = crc(received, divisor)

if '1' not in check:
    print("No Error Detected")
else:
    print("Error Detected")