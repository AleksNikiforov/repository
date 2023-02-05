class Array:
    """
    Линейный статический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def min(self):
        """
        Минимальное значение в массиве.
        """
        _min = self.data[0]
        for num in self.data[1:self.length]:
            if num < _min:
                _min = num
        return _min

    def max(self):
        """
        Максимальное значение в массиве.
        """
        _max = self.data[0]
        for num in self.data[1:self.length]:
            if num > _max:
                _max = num
        return _max

    def avg(self):
        """
        Среднее значение в массиве.
        """
        _summ = 0
        for num in self.data[:self.length]:
            _summ += num
        return _summ/self.length
            
    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


array = Array(6)
print(array.__str__())
print(array.size)
print(array.length)
array.append(7)
array.append(5)
array.append(9)
array.append(3)
print(array.__str__())
print(array.size)
print(array.length)
print(array.min())
print(array.max())
print(array.avg())