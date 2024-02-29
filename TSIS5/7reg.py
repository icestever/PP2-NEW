import re

def snake_to_camel(snake_case_str):
    camel_case_str = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case_str)
    return camel_case_str

snake_case_string = "snake_case_example"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)
