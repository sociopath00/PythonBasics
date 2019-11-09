"""
    @author: Akshay Nevrekar
    @created_on: 6th November,2019
    @last_updated_on: 6th November,2019
"""

# import module
import os

# get current directory
print(os.getcwd())

# create new directory
# if you want to create dir somewhere else give absolute path
os.mkdir("temp")

# list all the files
print(os.listdir())

# remove directory
os.rmdir("temp")

# rename the files or dir
os.rename("files", "datafiles")

# change current directory
os.chdir("..")
print(os.getcwd())

