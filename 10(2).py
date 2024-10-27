import os

file = open("files2.txt", "r")
direc = file.read().strip().split()
#print(direc)

lst = []

for dir_name in direc:
    dir_path = os.path.join("D:\\", dir_name)
    if os.path.isdir(dir_path):
        lst.append(dir_name)
print(lst)

with open("res.txt", "w") as output_file:
    for dir_name in lst:
        output_file.write(dir_name + "\n")