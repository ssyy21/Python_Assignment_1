#19. Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
    return ''.join([char for char in input_string if char not in string.punctuation])

test_string = "Hello, world! This is a test string with punctuation: commas, periods, exclamation marks, etc."
cleaned_string = remove_punctuation(test_string)
print(cleaned_string)
