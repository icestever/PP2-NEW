# polindrom
def pall(s):
    for x in range(len(s)//2):
        if s[x] != s[len(s) - x - 1]:
            return "No"
    return"Yes"  
s = input()
print(pall(s))
