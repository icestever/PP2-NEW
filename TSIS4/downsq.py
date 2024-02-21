def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Enter a number (n): "))

countdown_numbers = countdown_generator(n)

print(f"Numbers from {n} down to 0:")
for num in countdown_numbers:
    print(num)
