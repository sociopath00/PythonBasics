"""
    @author: Akshay Nevrekar
    @created_on: 6th November,2019
    @last_updated_on: 6th November,2019
"""

# import module
import re

"""
Identifiers

    \d -> any number
    \D -> anything but number
    \s -> space
    \S -> anything bus space
    \w -> any character
    \W -> anything but character
    .  -> any character except new line
    \b -> the whitespace around words
    \. -> .

Modifiers

    {1,3} 1-3
    + match 1 or more
    ? match 0 or 1
    * match 0 or more
    $ match end of a string
    ^ match the beginning of a string
    | either or or
    [] range
"""

statement = "PYTHON is a programming language but cat and rat are playing hide and seek. Is python popular?"
statement1 = "The earth is flat"
statement2 = "is it free?"

# find python in above statement
word = re.search(r"python", statement, re.IGNORECASE)
print(word)
print(word.group())

# # find all occurance
words = re.findall(r"python", statement, re.IGNORECASE)
print(words)

# find statements starts with `The`
pattern = "^The"
words = re.search(pattern, statement1, re.IGNORECASE)
print(words)

words = re.search(pattern, statement2)
print(words)

# check if str ends with `?`
pattern = ".*\?$"
words = re.search(pattern, statement1)
print(words)

words = re.search(pattern, statement)
print(words)
print(words.group())

# words = re.search(pattern, statement2)
# print(words)

## More
statement = "Raj is 17 years old and born in 2002 whereas Sameer is born in 1999 and 20. Jas is 7 years old where"

# find numbers
numbers = re.findall("\d", statement)
print(numbers)

numbers = re.findall("\d+", statement)
print(numbers)

years = re.findall("\d{2,4}", statement)
print(years)

names = re.findall("[A-Z][a-z]+", statement)
print(names)


print(re.findall(r"\bwhere\b", statement))
