a = [1, 3, 5, 7, 9, 11, 13, 15]

def boolean(lst, num):
    for elem in lst:
        if elem == num:
            return True
    return False

print(boolean(a, 0))


