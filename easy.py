#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alana
#
# Created:     28.11.2018
# Copyright:   (c) Alana 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#__author__ = 'Alana Daurova'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры числа числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с ризом для.

"""nomber = int(input('Введите произвольное целое положительное число: '))
for i in str(nomber):
    print(i)"""


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#    или через арифметические действия
# Не нужно решать задачу так:
# print ("a =", b, "b =", a) - это неправильное решение!

""""a = int(input('ведите проивольное числo: '))
b = int(input('ведите проивольное числo: '))
c = a
a = b
b = c
print("Значения после замены переменных: " "a =", a, "b =", b)"""

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input('ведите Ваш возраст: '))
if(age>=18):
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
