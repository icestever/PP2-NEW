def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number (n): "))

even_numbers = even_generator(n)

print("Even numbers:", end=" ")
print(*even_numbers, sep=", ")
