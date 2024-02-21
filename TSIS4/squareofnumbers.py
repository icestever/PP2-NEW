def squares_generator(N):
    for num in range(N):
        yield num ** 2

N = int(input())
squares = squares_generator(N)

for square in squares:
    print(square)
