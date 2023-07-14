# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


def number_from_user1() -> str:
    info = input("Пожалуйста, первую дробь в формате 'a/b' \n: ")
    a, b = info.split('/')
    return int(a), int(b)


def number_from_user2() -> str:
    info = input("Пожалуйста, вторую дробь в формате 'a/b' \n: ")
    c, d = info.split('/')
    int(c), int(d)
    return int(c), int(d)


def multiplication(a: int, b: int, c: int, d: int):
    num1 = a * c
    num2 = b * d
    return fractions.Fraction(num1, num2)


def division(a: int, b: int, c: int, d: int):
    num1 = a * d
    num2 = b * c
    return fractions.Fraction(num1, num2)


a, b = number_from_user1()
c, d = number_from_user2()

option: int = int(input("Выберите действие: \n 1. Умножение \n 2. Деление \n:"))

match option:
    case 1: print(f'{a}/{b}*{c}/{d} = {multiplication(a, b, c, d)}')
    case 2: print(f'{a}/{b}:{c}/{d} = {division(a, b, c, d)}')


