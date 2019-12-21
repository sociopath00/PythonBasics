# total_income = int(input("Enter total_income: "))
# parts = int(input("Enter no of parts: "))

# try:
#     salary = total_income/parts
#     print(salary)
# except ZeroDivisionError as e:
#     pass

# try:
#     print(salary)

# except NameError as e:
#     print(e)
# total_income = total_income * 1.05
# print(total_income)


# a = [1,2,3,4,5]

# #print(a[6])
# try:
#     print(a[6])
# except IndexError as e:
#     print(e)

# print(a)


# d = {"sam": 75, "dean": 60}
# try:
#     print(d["sam"])
# except KeyError as e:
#     print(e)

# finally:
#     print(d)



# a = [1,2,3,4,5]
# b = 0
# try:
#     temp = a[6]

#     try:
#         temp2 = temp/b
#     except ZeroDivisionError as e:
#         pass

# except IndexError as e:
#     print(e)
try:
    import aksahy
except ImportError as e:
    pass
