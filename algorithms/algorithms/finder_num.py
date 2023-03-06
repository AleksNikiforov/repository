def finder(array):
    '''поиск уникальных не повторящихся чисел больше 5'''
    uniq_num = []
    for n in array:
        if n < 5:
            continue
        if n not in uniq_num:
            uniq_num.append(n)
            continue
        if n in uniq_num:
            uniq_num.pop(uniq_num.index(n))
    return uniq_num

def test_finder():
    result  = finder([3, 2, -10, 2, 100, 45])
    assert result == [100, 45], f'Wrong answer: {result}'
    result = finder([100, 100, 99])
    assert result == [99], f'Wrong answer: {result}'
    result = finder([1])
    assert result == [], f'Wrong answer: {result}'
    result = finder([])
    assert result == [], f'Wrong answer: {result}'
    result = finder([1, 1, 7, 7, 8])
    assert result == [8], f'Wrong answer: {result}'
    result = finder([1, 2, 3, 4])
    assert result == [], f'Wrong answer: {result}'
    result = finder([1, 5, 8, 8, 10])
    assert result == [5, 10], f'Wrong answer: {result}'

if __name__ == '__main__':
    test_finder()