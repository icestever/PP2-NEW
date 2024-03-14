import os

with open('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', 'r') as f, open('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\demo.txt', 'a') as r:
    for i in f:
        r.write(i)

with open('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\demo.txt') as p:
    pr = p.read()
    print(pr)
    