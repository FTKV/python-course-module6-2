# with open("text.bin", "wb") as file:
#     file.write("Hello World")

# with open("text.bin", "wb") as file:
#     file.write(b"Hello World")

# with open("text.bin", "wb") as file:
#     file.write(b"Привіт Світ")

# with open("text.bin", "wb") as file:
#     file.write(bytes([256]))

# with open("text.bin", "wb") as file:
#      print(file.write("Привіт Світ".encode()))

# with open("text.bin", "rb") as file:
#      data = file.read()
#      for i in data:
#           print(i)

# for i in range(256):
#      print(i,"         ", bytes([i]).decode("ascii"))

with open("text.bin", "wb") as file:
    print(file.write("ПривітСвіт".encode("utf32")))