class MoneyBox:
    '''Виртуальная копилка с вместимостью capacity'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        self.v = v
        a = self.count + self.v
        if a <= self.capacity:
            return(True)
        else:
            return(False)

    def add(self, v):
        if self.can_add(v):
            self.count += v

'''
# Пример работы

x = MoneyBox(10)

x.add(5)
x.add(10)

print(x.count) # 5 (так как вместимость копилки 10, а пытаются положить 5 + 10 монет)
'''