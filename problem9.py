# Problem 9
import math
for a in range(1000):
	for b in range(1000):
		for c in range(1000):
			if (a + b + c) == 1000:
				if (a < b < c):
					if (math.pow(a, 2) + (math.pow(b, 2)) == math.pow(c, 2)):
						print ("========= MATCH ========")
						print ("A: " + str(a))
						print ("B: " + str(b))
						print ("C: " + str(c))
						print ("Product: " + str(a*b*c))
						print ("========================")
						quit()