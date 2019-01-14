"""
    Problem Statement :
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    Solution Design :
        Sine the number in question has to be be divisible by all the numbers then some of the properties of that number
        should be :

            1) Should end with Zero, such that it is evenly divisble by 10 or 20
            2) Should be greater then 20 :-D
            3) SHhould be even ending number such that it is part of the sequence 40,60,80.........

"""
# TODO : find way to reduce the computational time.

# we will start with 20
start_number = 20

while True:
    l = [start_number % x for x in range(1, 21)]
    if sum(l) == 0:
        break
    else:
        start_number = start_number + 20
print(start_number)
