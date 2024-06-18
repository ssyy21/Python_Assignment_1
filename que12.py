# 12. Write a python program that calculates the sum of the digits of a given number. 

num = int(input("Enter the number : "))


def sum_of_digit(num):
    sum = 0
    str1 = str(num)

    for digit in str1:
   
        sum += int(digit)
    return sum


ans = sum_of_digit(num)
print(ans)