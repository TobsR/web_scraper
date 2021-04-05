encode = list(str(input()))
key = int(input())

key_sum = sum((key).to_bytes(2, byteorder='little'))
result = ''
for x in encode:
    result += chr(ord(x) + key_sum)
print(result)
