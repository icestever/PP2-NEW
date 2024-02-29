import re

def insert_spaces_between_capital_words(input_str):
    # use regular expression to insert spaces between words starting with capital letters
    result = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', input_str)
    return result

# example usage
input_string = "InsertSpacesBetweenCapitalWords"
output = insert_spaces_between_capital_words(input_string)
print(output)
