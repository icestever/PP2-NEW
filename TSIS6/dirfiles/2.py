import os

print(os.access('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', os.F_OK))  ##TRUE
print(os.access('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', os.R_OK))  ###TRUE
print(os.access('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', os.W_OK))  ###TRUE
print(os.access('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\papapa.txt', os.X_OK))  ###TRUE
