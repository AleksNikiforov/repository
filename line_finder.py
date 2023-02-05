def lianer_search(values, target):
    '''Линейный поиск'''
    # i = 0
    # while i < len(values):
    #     if values[i] == target:
    #         return i
    #     i += 1
    # return -1

    for i, num in enumerate(values):
        if num == target:
            return i


def test_lianer_search():
    result  = lianer_search([3, 2, -10, 2, 100, 45], 45) 
    assert result == 5,  f'Wrong answer: {result}'
    result = lianer_search([1, 100, 99], 1)
    assert result == 0, f'Wrong answer: {result}'
    result = lianer_search([4, 5, 6, 19, 4, 6], 19)
    assert result == 3, f'Wrong answer: {result}'

if __name__ == '__main__':
    test_lianer_search()