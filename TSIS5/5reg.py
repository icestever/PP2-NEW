#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

if re.search('a.+b', text):
    print("Matches")
else:
    print("No matches")
