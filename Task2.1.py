# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BIN_DIVIDER = 2
OCT_DIVIDER = 8
SIXT_DIVIDER = 16


def get_number_from_user():
    info = input("Пожалуйста, введите число и делитель через запятую: ")
    r, d = info.split(',')
    return int(r), int(d)


def converter(patient: int, divider: int) -> tuple[int, int]:
    r: str = ''
    while patient > 0:
        res = patient % divider
        if divider == 16:
            if res == 10:
                res = "a"
            if res == 11:
                res = "b"
            if res == 12:
                res = "c"
            if res == 13:
                res = "d"
            if res == 14:
                res = "e"
            if res == 15:
                res = "f"
        r += str(res)
        patient //= divider
    return r[::-1]


patient, divider = get_number_from_user()
if isinstance(patient, int) and divider in (BIN_DIVIDER, OCT_DIVIDER, SIXT_DIVIDER):
    print(converter(patient, divider))
else:
    print("Неверный ввод")

print(hex(patient))
