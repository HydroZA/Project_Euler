# problem 14

def GetSequenceLen(n):
	chain_len = 0
	while n > 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = n*3 + 1
		chain_len += 1
	return chain_len + 1

longest_chain = 0
longest_chain_starting_num = 0
for i in range(0, 1_000_000):
	seq_len = GetSequenceLen(i)
	if seq_len > longest_chain:
		longest_chain_starting_num = i
		longest_chain = seq_len
	print("Progress: " + str(int(i/1_000_000*100)) + "%", end="\r")

print("\nThe starting number that produces the longest chain is: ")
print (str(longest_chain_starting_num))