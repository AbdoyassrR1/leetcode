#!/usr/bin/python3

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    strnums = ""
    for num in digits:
        num = str(num)
        strnums += num

    res = int(strnums) + 1
    res = str(res)
    new_list = []
    for num in res:
        new_list.append(int(num))
    return new_list


dig = [1,2,3]
print(plusOne(dig))
