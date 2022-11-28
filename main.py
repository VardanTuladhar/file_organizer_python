
import os
print("Hello and welcome to Vardan's File organizer")
#First step is to scan files and print their names
path = r"C:\Users\varda\Favorites\Downloads"
scanner = os.scandir(path)
print("Files and Directories in " + path)
for file in scanner:
    if file.is_dir() or file.is_file():
        print(file.name)
    