# Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# matches = 0
# a = 2090618

# while True:
# 	try:
# 		print ("A: " + str(a))
# 		for b in range (2, 21):
# 			print ("B: " + str(b))
# 			if a % b == 0:
# 				matches += 1
# 				if matches == 19:
# 					print ("MATCH: " + str(a))
# 					quit()
# 			else:
# 				print ("matches successful: " + str(matches))
# 				matches = 0
# 				a+=1
# 				break
# 	except KeyboardInterrupt:
# 		print ("Most matches: " + str(matches) + " on " + str(a))
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(2520)
    if solution is None:
        print ("No answer found")
    else:
        print ("found an answer:" +  str(solution) )