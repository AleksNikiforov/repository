num = input()

list_of_num = num.split()

length_of_list = len(list_of_num)


if len(list_of_num) < 2:
    print('YES')
elif len(set(list_of_num)) == 1:
    print("YES")
else:
    for n in range(length_of_list - 1):
        if list_of_num[n] >= list_of_num[n + 1]:
            yes = True
        else:
            yes = False
            break
    if yes:
        print('YES') 
    else:  
        for n in range(length_of_list - 1):
            if list_of_num[n] <= list_of_num[n + 1]:
                yes = True
            else:
                yes = False
                break
        if yes:
            print('YES')
        else:
            print('NO')
