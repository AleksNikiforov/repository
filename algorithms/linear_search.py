def linear_search(lst, val):
    for idx, num in enumerate(lst):
        if num == val:
            return idx
    return -1

            


idx = linear_search([1, 2 ,3 ,4], 3)
print(idx)