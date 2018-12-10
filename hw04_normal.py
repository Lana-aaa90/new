# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
"""

line = "mtMmEZUOmcq"

# без использования re
list1 = list(line)
list2 = []
for el in list1:
    if el.isupper():
        list2.append('_')
    else:
        list2.append(el)

line_new = ''.join(list2)
list2 = line_new.split('_')
list2 = [item for item in list2 if item != '']
print(list2)


# с использованием re
import re
match = re.findall("[a-z]+", line)
print(match)

"""
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
"""
line = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
s = ""
list2 = []
for el in line:
    if el.isupper():
        if len(s) < 2:
            s = ""
        elif len(s) >= 2:
            s += el
    if el.islower():
        if len(s) < 2:
            s += el
        elif len(s) >= 5:
            list2.append(s[2:-2])
            s = el
        elif s[-1].isupper():
            s = el
print(list2)
"""

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

