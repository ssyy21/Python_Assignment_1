#25. Write a program that copies the contents of one text file to another. 
source_file = 'D:\Python and ML\Assignment_1\source.txt'
destination_file = 'D:\Python and ML\Assignment_1\destination.txt'
def copy_file_content(source_file, destination_file):
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            dest.write(src.read())


copy_file_content(source_file, destination_file)
print(f"Content copied from {source_file} to {destination_file}")
