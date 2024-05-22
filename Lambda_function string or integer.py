### Write a python code using lambda function to check every 
# element of a list is an integer or string ? 

# Input list
my_list = [40, "shruti", 5.5, "jalikatti", 20]

# Lambda function to check if element is integer or string
check_type = lambda x: isinstance(x, (int, str))

# Check if every element in the list is an integer or string
result = all(map(check_type, my_list))

# Print the result
print(result)


