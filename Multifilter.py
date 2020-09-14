'''

Multifilter

В качестве аргументов принимает список чисел, функций фильтров и функцию-судью,
решающую о выводе или не выводе числа
'''

class Multifilter:

    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos < neg:
            # Удалить
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos < 1:
            # Удалить
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg > 0:
            # Удалить
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.results = {}

    def __iter__(self):
        # возвращает итератор по результирующей последовательности

        # func - функция из кортежа функций funcs.
        # Каждая функция func - ключ словаря results.
        # Каждый ключ results содержит значения вызова
        # функций от числа из списка чисел iterable.
        for func in self.funcs:
            self.results[func] = []
            for i in self.iterable:
                self.results[func] += [func(i)]
        # Для каждого числа списка iterable проверяем
        # значения каждой фукнции (True или False)
        # и считаем количество pos и neg.
        for i in range(len(self.iterable)):
            pos, neg = 0, 0
            for func in self.funcs:
                if self.results[func][i] == True:
                    pos += 1
                else:
                    neg += 1
            # В зависимости от выбранной функции-судьи, принимается
            # решение о выводе или не выводе числа.
            if self.judge(pos, neg) == False:
                yield i

'''

# Демонстрационный вариант работы класса Multifilter

# Определение функций-фильтров
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

# Список чисел
a = [i for i in range(31)]

# Вывод списка чисел, прошедших фильтр 
print(list(Multifilter(a, mul2, mul3, mul5)))

'''