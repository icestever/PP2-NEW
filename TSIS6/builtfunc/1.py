
def umnozh(n):
    num = 1
    for i in n:
        num *= i
    return num
print(umnozh((1, 2, 3, 5)))