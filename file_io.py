"""
    @author: Akshay Nevrekar
    @created_on: 6th November,2019
    @last_updated_on: 6th November,2019
"""

# open the existing file
f = open("datafiles/abc.txt", "r")

# read content from file
# print(f.read())

# read only 10 character from the file
c1 = f.read(10)
print(c1)

# read next 10 char
c2 = f.read(10)
print(c2)

# find the location of pointer
print(f.tell())

# reset the pointer
f.seek(0)

print(f.tell())

# read content line by line
lines = f.readlines()

print(lines)

# close file
f.close()

# create new file
f = open("datafiles/temp.txt", "w")

strings = "I am working with Python."

# write string in file
f.write(strings)

lists = ["a", "b", "c", "d"]
for i in lists:
    f.write(i+"\n")

f.close()

