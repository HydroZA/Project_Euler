# Problem 1
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def NaturalNumberSumFinder(highest):
	multiples = []
	for i in range(0, highest):
		if (i%3) == 0:
			multiples.append(i)
		elif (i%5) == 0:
			multiples.append(i)
	return multiples

multiples = NaturalNumberSumFinder(1000)
sum_of_multiples = 0
for multiple in multiples:
	sum_of_multiples += multiple
print (sum_of_multiples)