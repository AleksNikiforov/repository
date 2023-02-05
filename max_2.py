def two_max(array):
    '''поиск второго макисмального числа'''
    if len(array) == 2 and array[0] == array[1] or len(array) == 1:
        return None
    else:
        try:
            if array[0] > array[1]:
                max_1, max_2 = array[0], array[1]
            else:
                max_1, max_2 = array[1], array[0]
        except Exception as e:
            return None

        for n in array[2:]:
            if n > max_1:
                max_2 = max_1 #3
                max_1 = n     #100
            elif n > max_2:
                max_2 = n
            elif n < max_1:
                max_2 = n
            else:
                continue
        return max_2

def test_two_max():
    result  = two_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong answer: {result}'
    result = two_max([100, 100, 99])
    assert result == 99, f'Wrong answer: {result}'
    result = two_max([1])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([1, 1, 7, 7, 8])
    assert result == 7, f'Wrong answer: {result}'
    result = two_max([1, 1])
    assert result == None, f'Wrong answer: {result}'
    result = two_max([1, 2])
    assert result == 1, f'Wrong answer: {result}'

if __name__ == '__main__':
    test_two_max()