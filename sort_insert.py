def insertionsort(array):
    """
    Сортировка массива array вставками.
    """

    # Перебираем все элементы массива начиная со второго.
    i = 1
    while i < len(array):
        j = i - 1
        # Проходим по отсортированной части в обратную строну.
        # До тех пор пока значение текущего элемента array[j + 1]
        # меньше значения предыдущего array[j].
        while array[j + 1] < array[j] and j >= 0:
            # Меняем элементы местами.
            array[j + 1], array[j] = array[j], array[j + 1]
            j -= 1
        i += 1


array = [7, 8, 5, 4, 9, 2]
print(array)
insertionsort(array)
print(array)