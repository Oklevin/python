"""
Задание  5.
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введён после нескольких чисел, то
вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
этого завершить программу.
"""


summary = 0
is_ok = True


def my_sum(string_nums, start_sum):
    """
    Суммирует  все числа в строке
         и прибавляет к ранее вычисленному результату.
    """
    for num in string_nums.split(' '):
        try:
            start_sum += float(num)
        except Exception:
            return start_sum, False
    return start_sum, True


while is_ok:
    summary, is_ok = my_sum(input('Введите числа через пробел: '), summary)
    print(summary)
