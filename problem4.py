# Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

highest = 0
for a in range (100, 1000):
	for b in range (100, 1000):
		x = str(a * b)
		rev_x = ''.join(reversed(x))
		if x == rev_x:
			x = int (x)
			if x > highest:
				highest = x

print (highest)