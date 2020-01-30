# Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

# get all factors of 600851475143 in factor_array
# for i in factor_array:
	# if i is prime:
		#add to prime_factor_array
#answer = prime_factor_array[len(prime_factor_array)-1]

# def GetFactorsOf(n):
# 	i = 1
# 	factor_array = []

# 	while i <= n:
# 		if (n % i) == 0:
# 			factor_array.append(i)
# 			print ("Got factor: " + str(i))
# 		print ("Progress: " + str(i(i/n)*100), end="\r")
# 		i+=1
# 	return factor_array
# def IsPrime(n):
# 	if n <= 3:
# 		return n > 1
# 	elif ((n % 2) == 0 or (n%3) == 0):
# 		return false
# 	i = 5
# 	while i * i <= n:
# 		if (n%i) == 0 or (n%(i+2)) == 0:
# 			return false
# 		i = i + 6
# 	return true

# factor_array = GetFactorsOf(600851475143)
# prime_factor_array = []

# for factor in factor_array:
# 	if IsPrime(factor):
# 		prime_factor_array.append(factor)

# answer = prime_factor_array[len(prime_factor_array)-1]
# print (str(answer))

n = 600851475143 
p = 2
while n >= (p*p):
	if (n%p==0):
		n = n/p
	else:
		p +=1
print (n)