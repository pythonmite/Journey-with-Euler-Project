"""
    Problem Statement :

        The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

        Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000***1000.
"""

# list comprehensions
raised_elements = [x**x for x in range(1, 1001)]
result = sum(raised_elements)

# type casting
result = str(result)[-10:]
print(result)
# Answer 9110846700