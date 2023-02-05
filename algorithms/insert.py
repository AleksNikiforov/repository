class Array:
    """
    Линейный ститический массив.

    Запрограммируйте метод insert для вставки элементов в середину массива.
    Метод должен принимать два аргумента: индекс для вставки и значение нового элемента.
    В случае если массив полностью заполнен, при вставке нового значения должно срабатывать исключение OverflowError.
    В случае если индекс выходит за пределы массива, то новый элемент должен добавляться в конец.

    При вставке элемента на позицию i, все элементы начиная с этой позиции должны быть смещены вправо.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
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

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """

        if self.length >= self.size:
            raise OverflowError

        elif index > self.length:
            self.append(value)

        else:
            i = self.length
            while i > index:
                self.data[i] = self.data[i-1]
                i -= 1
            self.data[index] = value
            self.length += 1
        return self.data

        
    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
        