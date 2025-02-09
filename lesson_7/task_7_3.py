"""
Задание 3.
Реализовать программу работы с органическими клетками, состоящими
из ячеек. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству ячеек клетки
(целое число). В классе должны быть реализованы методы перегрузки
арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы
должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей
клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять
только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей
клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей
клетки определяется как целочисленное
деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то
в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12,
количество ячеек в ряду — 5. Тогда метод make_order()
вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество
ячеек в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell():
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f"Сумма {self.num} + {other.num} = {self.num + other.num}"

    def __sub__(self, other):
        return self.num - other.num if self.num - other.num > 0 \
            else "Ячеек в первой клетке меньше или равно второй"

    def __mul__(self, other):
        return f"Умножение {self.num} * {other.num} = {self.num * other.num}"

    def __truediv__(self, other):
        if other.num != 0:
            r = f"Деление {self.num} / {other.num}= {self.num / other.num:.3f}"
            return r
        else:
            return "Делить на ноль нельзя"

    def make_order(self, rows):
        result = "\n".join(["*" * rows for i in range(self.num // rows)]) \
            + "\n" \
            + "*" * (self.num % rows)
        return result


c_1 = Cell(10)
c_2 = Cell(44)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_2.make_order(10))
