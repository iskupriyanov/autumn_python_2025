#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

f = open('inverted_sort.txt', encoding='utf-8', mode='r+', newline='')
lines = f.readlines()
reversed_line = lines [::-1]
reversed_line = [line if line.endswith('\n') else line + '\n' for line in reversed_line]

f = open('inverted_sort.txt', encoding='utf-8', mode='a', newline='')
f.writelines(reversed_line)
f.close()