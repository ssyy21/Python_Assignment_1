#15.Write a program that reads data from a CSV file and prints it to the console
import csv
with open('D:\Python and ML\Assignment_1\demo2.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
