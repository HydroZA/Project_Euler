# # # problem 12
# # highest: 6699630
#17907120 = 480 factors


#from sympy.ntheory import factorint
from primefac import factorint
from primefac import *
from functools import reduce
import math

def divisorGen(n):
	n = 100
	factors = factorint(n, trial_limit=1000, rho_rounds=42000, methods=(pollardRho_brent, pollard_pm1, williams_pp1, ecm, mpqs))
	print (n)
	print(factors)
	nfactors = len(factors)
	f = [0] * nfactors
	while True:
		yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
		i = 0
		while True:
			f[i] += 1
			if f[i] <= factors[i][1]:
				break
			f[i] = 0
			i += 1
			if i >= nfactors:
				return

x = 1
y = 2

while True:
	#factors = 0
	x = x + y
	

	# for z in range(1, x+1):
	# 	if x % z == 0:
	# 		factors += 1

	factors = list(divisorGen(x))
	print (factors)

	print (str(x) + " has " + str(factors) + " factors")
	if factors > 500:
		print ("========== MATCH ==========")
		print (str(x) + " is the magic number")
		print ("With " + str(factors) + " factors")
		print ("===========================")
		quit()
	y+=1
