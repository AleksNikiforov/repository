def selection_sort(values):
    '''Сортировка выбором'''
    for i in range(len(values) - 1):
        min_index_of_list = i
        for j in range(i + 1, len(values)):
            if values[min_index_of_list] > values[j]:
                min_index_of_list = j
        if i != min_index_of_list:
            values[i], values[min_index_of_list] = values[min_index_of_list], values[i]
    return values


def test_selection_sort():
    result  = selection_sort([7, 8, 2, 5, 3, 6, 1, 9]) 
    assert result == [1, 2, 3, 5, 6, 7, 8, 9],  f'Wrong answer: {result}'


if __name__ == '__main__':
    test_selection_sort()