def divisible_by_three_and_four_generator(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number (n): "))

divisible_numbers = divisible_by_three_and_four_generator(n)

print("Numbers divisible by 3 and 4:", end=" ")
print(*divisible_numbers, sep=", ")
