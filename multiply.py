# def multiply(x, y):
#     total = 0
#     while x > 0:
#         total += y
#         x -= 1
#     return total


def multiply(x, y):
    total = 0

    if x < 0:
        x = -x
        return 0

    if y < 0:
        y = -y
        return 0

    while x > 0:
        total += y
        x -= 1

    return total 
print (multiply(27, -3))