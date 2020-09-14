class Buffer:
    '''
    Класс Buffer реализует сложение первых 5 чисел и вывод их на экран.
    Если чисел больше, то они заносятся в память и хранятся до тех пор, пока не будет
    5 чисел для сложения
    '''
    def __init__(self):
        self.memory = []

    def add(self, *a):
        self.a = a
        self.memory += a
        while len(self.memory) >= 5:
            self.sum = 0
            for i in range(5):
                self.sum += self.memory[i]
            print(self.sum)
            self.memory = self.memory[5:]

    def get_current_part(self):
        return(self.memory)

'''
Пример использования

x = Buffer()

x.add(1, 2, 3)
x.get_current_part() # memory хранит 3 значения

x.add(4, 5, 6)
x.get_current_part() # вывод на экран суммы первых 5 чисел: 1, 2, 3, 4, 5

x.add(7, 8, 9, 10)
x.get_current_part() # вывод суммы чисел от 6 до 10

x.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
x.get_current_part() # вывод двух сумм пяти единиц, и в memory сохраняется одна единица
'''