# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
"""
def my_round(number, ndigits):
    temp_numb = number*(10**ndigits)
    temp_numb = temp_numb + 0.41
    int_number = temp_numb//1
    float_number = int_number/(10**ndigits)
    return float_number
float_number = my_round(5.123456789,2)
print(float_number)
"""
# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def my_happy_ticket(number):
    my_happy_ticket_str = str(number)
    t1 = my_happy_ticket_str[:3]
    t2 = my_happy_ticket_str[3:]
    sum1 = 0
    for el in t1:
        sum1 = sum1 + int(el)
    sum2 = 0
    for el in t2:
        sum2 = sum2 + int(el)
    if sum1 == sum2:
        res_mes = "Ура! У Вас счастливый билет"
    else:
        res_mes = "Вам не повезло"
    return res_mes

res = my_happy_ticket(input("Введите шестизначный номер своего билета:"))
print(res)





