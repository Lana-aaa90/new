# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
"""
def fibonacci(n, m):
    fib_list = [1, 1, 2]
    n1 = 1
    n2 = 1
    n3 = 2
    i = 3
    while i < m:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        fib_list.append(n3)
        i += 1
    return fib_list[n-1:]

fib = fibonacci(1, 10)
print(fib)

"""


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def bubble(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst [i + 1]:
                lst[i], lst [i + 1] = lst [i + 1], lst[i]
    n += 1
    return lst

lst = [25, 45, 3, 15, 41, 35, -3, 5, 10]
print("Было ---> {} Пузырьки всплыли ---> {}".format(lst, bubble(lst[:])))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
"""
lost = [15, 14, 99, 99, 1, 30, 98, -4, 4, 4, 4, -5, 100]
def filt(arg, obj):
    print(obj)
    lst = []
    for i in obj:
        if i != arg:
            lst.append(i)
    print(lst)
filt(99, lost)
"""
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
"""
x1 = 2
x2 = 2
x3 = 4
x4 = 4
y1 = 2
y2 = 2
y3 = 4
y4 = 4
A1 = [x1, y1]
A2 = [x2, y2]
A3 = [x3, y3]
A4 = [x4, y4]
# AO = OC OC = OD диагонали параллелограмма точкой перечечения делятся пополам
O1 = [(A3[0] + A1[0])/2, (A3[1] + A1[1])/2]
O2 = [(A4[0] + A2[0])/2, (A4[1] + A2[1])/2]
if A3[0] - A2[0] == A4[0] - A1[0] and A2[1] - A1[1] == A3[1] - A4[1] and O1[0] == O2[0] and O1[1] == O2[1]:
    print("Это параллелограмм")

else:
    print("это не параллелограмм")

    """