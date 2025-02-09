"""
Задание 4.
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс
«Оргтехника», который будет базовым для
классов-наследников. Эти классы — конкретные
типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие
для приведённых типов. В классах-наследниках
реализуйте параметры, уникальные для каждого типа оргтехники.

---
Продолжить работу над первым заданием. Разработайте
методы, которые отвечают за приём оргтехники на
склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать
любую подходящую структуру (например, словарь).
---
Продолжить работу над вторым заданием. Реализуйте
механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {
            'Модель устройства': self.name,
            'Цена за ед': self.price,
            'Количество': self.quantity
        }

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print('Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input('Введите наименование ')
            unit_p = int(input('Введите цену за ед '))
            unit_q = int(input('Введите количество '))
            unique = {
                'Модель устройства': unit,
                'Цена за ед': unit_p,
                'Количество': unit_q
            }
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except Exception:
            return 'Ошибка ввода данных'

        print('Для выхода - Q, продолжение - Enter')
        q = input('---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return 'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
