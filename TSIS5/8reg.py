import re

def split_string_at_uppercase(input_string):

    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result

input_string = "SplitThisStringAtUppercaseLetters"
output = split_string_at_uppercase(input_string)
print(output)
