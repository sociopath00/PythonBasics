"""
    @author: Akshay Nevrekar
    @created_on: 21st July,2019
    @last_updated_on: 4th November,2019
"""

a = 3
b = 6


# bitwise AND
# a      = 0000 0101(binary)
# b      = 0000 0011(binary)
# result = 0000 0001
print("Bitwise AND operation: ", a & b)


# bitwise OR
# a 	= 0000 0101
# b 	= 0000 0011
# result= 0000 0111
print("Bitwise OR operation: ", a | b)


# biwise XOR  (if both values are same then 0 else 1)
# a 	= 0000 0101
# b 	= 0000 0011
# result= 0000 0110
print("Bitwise XOR operation: ", a ^ b)


# left shift
# The left operand value is moved left by the number of bits present in the right operand.
print("Left shift operation: ", a<<b)


# right shift
# The left operand is moved right by the number of bits present in the right operand.
print("Right shift operation: ", a>>b)
