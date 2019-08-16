"""
    Problem Statement :
    
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    
    Solution design :
    
        Create a prime number checker.
"""
from math import sqrt; from itertools import count, islice


def prime_check_number(number):
    # https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
    return number > 1 and all(number%i for i in islice(count(2), int(sqrt(number)-1)))


def main(start_point, end_point):
    print('Start_point : {0}'.format(start_point))
    print('End point : {0}'.format(end_point))
    ans = sum(filter(prime_check_number, range(start_point, end_point)))
    return ans


if __name__ == '__main__':
    
    start_point = 1
    end_point = 10_000
    ans_list = []
    for i in range(2, 202):   
        ans_list.append(main(start_point, end_point))
        start_point = end_point
        end_point = i * 10000
    print(sum(ans_list))
    # ans 142913828922
        
    