"""
    @author: Akshay Nevrekar
    @created_on: 6th November,2019
    @last_updated_on: 6th November,2019
"""

# import module
import os

# get current directory
print(os.getcwd())

# with open("temp.txt", "w") as f:

# # create new directory
# # if you want to create dir somewhere else give absolute path
# os.mkdir("temp1")

# list all the files
print(os.listdir())

# # remove directory
# os.rmdir("temp1")

# # rename the files or dir
# os.rename("temp.txt", "new.txt")

# os.remove("new.txt")

# # change current directory
os.chdir("datafiles")
print(os.getcwd())


