# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix


input_string = "hello world"
prefix = "hello"
suffix = "world"

starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)

print(f"Does the string start with '{prefix}'? {'Yes' if starts_with_prefix else 'No'}")
print(f"Does the string end with '{suffix}'? {'Yes' if ends_with_suffix else 'No'}")
