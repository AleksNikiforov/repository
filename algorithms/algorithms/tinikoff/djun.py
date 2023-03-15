num = input()

list_of_num = num.split()

n = int(list_of_num[0])
m = int(list_of_num[1])
k = int(list_of_num[2])

if k == 0:
    print('0')
else:
    full_time = int((n * k)/m)
    if (n * k)%m != 0:
        full_time += + 1
    print(full_time)