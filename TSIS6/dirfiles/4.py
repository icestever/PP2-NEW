with open('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', 'r') as fcc_file:
    file = fcc_file.read()
    l = 0
    for string in file:
        l += len(string.split())
    print(l)