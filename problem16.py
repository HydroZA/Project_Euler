# Problem 16

import math

num = (str(2**1000))

sum_of_digits = 0
for i in num:
	sum_of_digits += int(i)
	
print (str(sum_of_digits))