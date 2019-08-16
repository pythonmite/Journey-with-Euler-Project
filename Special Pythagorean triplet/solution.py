"""
    Problem Statment :
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a2 + b2 = c2
        For example, 32 + 42 = 9 + 16 = 25 = 52.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
        
        
    Solution design: 
    
        (num+dig+i)2=10002
        Expand:
        num2+dig2+i2+2numdig+2numi+2digi=1000000
        Use triplet equality:
        2i2+2numdig+2numi+2digi=1000000
        Factor:

        i(num+dig+i)+numdig=500000
        Use fact that num+dig+i=1000 in our case:

        numdig+1000i=500000

    
"""

for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num * num + dig * dig == i * i:
            print(num, dig, i)
            print("Product: {}".format(num * dig * i))
            
# ans : 31875000
            