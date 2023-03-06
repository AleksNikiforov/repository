def compound(amount, year_percent, month):
    '''Вычисление сложных процентов'''
    month_percent = year_percent / 12
    for i in range(month):
        inc = amount / 100 * month_percent
        amount += inc
    return int(amount)


def compound_fast(amount, year_percent, month):
    '''Вычисление сложных процентов'''
    month_percent = year_percent / 12
    return amount + (1 + month_percent / 100) ** month


def test_persent():
    result  = compound(100000, 10, 12)
    assert result == 110471, f'Wrong answer: {result}'


if __name__ == '__main__':
    test_persent()
    print(compound(100000, 10, 12))