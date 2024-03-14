import string

for abc in string.ascii_uppercase:
    with open(abc + '.txt', 'a') as r:
        r.writelines(abc)

