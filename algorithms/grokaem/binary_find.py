def find_num(data, value):
    min = 0
    max = len(data) - 1
   

    while min <= max:
        middle = int((max + min) / 2)
        attemp = data[middle]

        if attemp == value:
            return middle
        elif attemp > value:
            max = middle - 1
        else:
            min = middle + 1
    return None


data = [1, 2, 3, 4, 6, 8 ,9]
num = find_num(data, 5)
print(num)
