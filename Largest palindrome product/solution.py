"""
    Problem Statement :
        A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
        numbers is 9009 = 91 × 99.

        Find the largest palindrome made from the product of two 3-digit numbers.
"""

# first we will calculate all the palindrome between 100 to 999 since they want the largest palindrome product for 3-digit number

palidrome_product_list = [i*j for i in range(1000, 100, -1) for j in range(1000, 100, -1) if str(i*j)[::] ==
                          str(i*j)[::-1]]
print(max(palidrome_product_list))
#Answer 906609