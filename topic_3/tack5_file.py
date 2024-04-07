# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!!')
# print(symbols_written) # 6
# fh.close()

# fh = open('test.txt', 'w+')
# fh.write('hello!!')
# fh.seek(0)
#
# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'
#
# fh.close()


# fh = open('test.txt', 'w')
# fh.write('hello!')
# fh.close()
#
# fh = open('test.txt', 'r')
# while True:
#     symbol = fh.read(1)
#     if len(symbol) == 0:
#         break
#     print(symbol)
#
# fh.close()

# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()
#
# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)
#
# fh.close()

# fh = open("test.txt", "w+")
# fh.write("hello!")
#
# position = fh.tell()
# print(position)  # 6
# fh.seek(1)
# position = fh.tell()
# print(position)  # 1
# fh.read(2)
# position = fh.tell()
# print(position)  # 3
#
# fh.close()

# s = b'Hello!'
# print(s[3])  # Виведе: 101 (це ASCII-код символу 'e')


# # Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел
# for num in [127, 457, 156]:
#   print(hex(num))

#
# s = "Привіт!"
#
# utf8 = s.encode()
# print(f"UTF-8: {utf8}")
#
# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")
#
# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")
#
# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)



byte_array = bytearray(b'Kill Bill')
byte_array[3] = ord('B')
# byte_array[5] = ord('K')
print(byte_array)

import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')


import shutil

# Створення TAR.GZ архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')
