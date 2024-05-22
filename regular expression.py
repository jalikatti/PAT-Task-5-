### Write a python function to validate the regular expression for the following
# a. Email address 
# b. mobile number of Bangladesh
# c. Telephone numbers of USA
# d. 16 character alpha numeric password composed of 
# alphabets of upper case, lower case, special characters, numbers

import re

def validate_input(input_str):
    # Regular expressions
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    bangladesh_mobile_regex = r'^\+?(88)?01[0-9]{9}$'
    usa_telephone_regex = r'^\+?1?[2-9]\d{2}[2-9](?!11)\d{6}$'
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'

    # Validation
    if re.match(email_regex, input_str):
        return "Email address is valid."
    elif re.match(bangladesh_mobile_regex, input_str):
        return "Mobile number of Bangladesh is valid."
    elif re.match(usa_telephone_regex, input_str):
        return "Telephone number of USA is valid."
    elif re.match(password_regex, input_str):
        return "Password is valid."
    else:
        return "Input does not match any valid format."

# Test cases
print(validate_input("xyz@example.com"))
print(validate_input("+8801234567890"))
print(validate_input("+12123456789"))
print(validate_input("shru181991JALIKATTI??$$"))
