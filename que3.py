# 3. Write a python program that calculates the factorial of a given number.

num= int(input("Enter the number : "))
def factorial(num):
    if(num==0):
        return 1
    return num*factorial(num-1)
ans = factorial(num)

print("Factorial : " , ans)