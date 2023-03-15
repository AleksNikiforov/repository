len_of_str = int(input())
a = input()

spisok = list(a)


print(spisok)

if 'a' not in spisok or 'b' not in spisok or 'c' not in spisok or 'd' not in spisok:
    print('-1')

# for n in range(len_of_str ):
#     if 'a' in spisok:

    a_indices = [i for i in range(0, len_of_str) if spisok[i]=="a"]
    list_temp = a_indices[-1]
    b_indices = [i for i in range(0, len_of_str) if spisok[i]=="b"]
    c_indices = [i for i in range(0, len_of_str) if spisok[i]=="c"]
    d_indices = [i for i in range(0, len_of_str) if spisok[i]=="d"]
    print(a_indices, b_indices, c_indices, d_indices)

    len_a = len(a_indices)
    len_b = len(b_indices)
    len_c = len(c_indices)
    len_d = len(d_indices)

    for a in range(len_a):
        new_list = []
        if a_indices[a] == b_indices[a] + 1:
            new_list.append(a_indices[a], )
            
            or a_indices[a] == b_indices - 1




else:
    for n in range(len_of_str):
        spisok[n]