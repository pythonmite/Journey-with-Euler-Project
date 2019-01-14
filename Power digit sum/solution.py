"""
    Problem Statement :
        2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

        What is the sum of the digits of the number 2**1000?

"""

# use of type casting
a = str(2**1000)

# Use 'map' function to convert str into a list of individual numbers
a = list(map(int, a))

# Use sum function to calculate the sum of the list
result = sum(a)
print(result)

# Answer 1366

