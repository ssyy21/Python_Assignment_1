# 16 .Write a program in python that counts the frequency of each character in a string. 
def count_character_frequency(input_string):
    frequency_dict = {}

    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

input_string = "hello world"
frequency = count_character_frequency(input_string)

for char, freq in frequency.items():
    print(f"'{char}': {freq}")
