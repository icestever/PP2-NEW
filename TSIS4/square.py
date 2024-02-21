def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the start value (a): "))
b = int(input("Enter the end value (b): "))

squares = squares_generator(a, b)

print(f"Squares of numbers from {a} to {b}:")
for square in squares:
    print(square)
