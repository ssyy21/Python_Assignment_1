# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines. 
lines = []
print("Enter multiple lines of text. Enter an empty line to stop:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
print(*lines, sep="\n", end="\n")
