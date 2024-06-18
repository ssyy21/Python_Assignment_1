# 5. Write a program that takes a string input from the user and writes it to a text file. 
str = "This is my new text file"
file= open("demo1.txt",'w')
file.write(str)
print("Text written successfully")
