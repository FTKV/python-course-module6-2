text = "Hello"
byte_text = b"Hello"

print(text)
print(byte_text)

for i in text:
    print(i)

for i in byte_text:
    print(i)

print(text[1])
print(byte_text[1])

for i in byte_text:
    print(hex(i))

print(text == byte_text)
print(text.encode() == byte_text)
print(text == byte_text.decode())