def linear_search(lst, val):
    num_of_find = []
    for idx, num in enumerate(lst):
        if num == val:
            num_of_find.append(idx)
    if num_of_find:
        return num_of_find
    else:
        return -1

            


idx = linear_search([1, 3 ,3 ,4], 3)
print(idx)

idx = linear_search([1, 3 ,3 ,4], 5)
print(idx)