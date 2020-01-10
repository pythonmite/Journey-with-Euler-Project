'''
    Problem Statement :
        n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(n):    # Recursion
    if n <= 1:
        return n
    else:
        return n*factorial(n-1)

result = factorial(100)

#type cating
list =[]

res = str(result)
for i in res:
    list.append(int(i))
sum = sum([i for i in list])
print(sum)   

    

#answer --> 648 