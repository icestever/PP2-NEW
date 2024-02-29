import re

def camel_to_snake(camel_case_str):
    #use regular expression to convert camel case to snake case
    snake_case_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case_str).lower()
    return snake_case_str

#primer
camel_case_string = "camelCaseExample"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)
