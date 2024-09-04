def check(list):
    if list[0] == list[-1]:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print(check(numbers_x))
print(check(numbers_y))
