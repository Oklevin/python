"""
Задание 2.
Создайте собственный класс-исключение, обрабатывающий
ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            result = divider / denominator
            return result
        except Exception:
            return ("Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
