def max(data):
    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max


print(max([1,2,3,4,5,7,8,6,4,3,2]))
