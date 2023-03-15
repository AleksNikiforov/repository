d = {'a' : 22, "b" : 45, "c" : 4, "d" : 55}
c = {'a' : 22, "b" : 45}

def find_two_max(data: dict):
    items = list(data.items())
    print(items)
    if len(data) < 3:
        return list(data.keys())
    max_1 = items[0][1]
    index_1 = items[0][0]
    print(max_1)
    count = 0
    maximums = []
    for n in items:
        count += 1
        if n[1] > max_1:
            max_1 = n[1]
            index_1 = n[0]
    items.pop(count)
    maximums.append(index_1)
    print(maximums)
    




print(find_two_max(d))
