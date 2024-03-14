


   






with open('papapa.txt', 'r') as f, open('demo.txt', 'a') as r:
    for i in f:
        r.write(i)

with open('demo.txt') as p:
    pr = p.read()
    print(pr)
    
import os
if os.path.exists('delete.txt') == True:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'delete.txt')
    os.remove(path)
else:
    print("NOT FOUND")
