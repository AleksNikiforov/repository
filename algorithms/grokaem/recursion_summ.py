# расчет суммы списка чисел при помощи рекурсии
def summ(data: list):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        return data[0]
    else:
        num = data[0]
        return num + summ(data[1:])
    

print(summ([1,2,3,4,5]))
    



