import os
if os.path.exists('C:\\Users\\aisul\\OneDrive\\Рабочий стол\\delete.txt') == True:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'C:\\Users\\aisul\\OneDrive\\Рабочий стол\\delete.txt')
    os.remove(path)
else:
    print("NOT FOUND")