def avg_temp_2(t):
    return sum(map(lambda x : float(x) ** 3, t)) / len(t)

def avg_temp_3(t):
    temp = (float(i) ** 3 for i in t)
    return sum(temp)/ len(t)


data = [1,2,3,4,5,6]
print(avg_temp_2(data))
print(avg_temp_3(data))
