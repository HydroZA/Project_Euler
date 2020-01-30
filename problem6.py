# Problem 6

#The sum of the sum_of_the_squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the sum_of_the_squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the sum_of_the_squares of the first one hundred natural numbers and the square of 


import math
sum_of_the_squares = 0
square_of_the_sum = 0

for i in range(1, 101):
	sum_of_the_squares += math.pow(i, 2)

for i in range(1, 101):
	square_of_the_sum += i
square_of_the_sum = math.pow(square_of_the_sum, 2)

print (str(square_of_the_sum - sum_of_the_squares))