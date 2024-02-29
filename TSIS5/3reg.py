#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

if re.search('[a-z]+_[a-z]', text):
    print("Matches")
else:
    print("No matches")
