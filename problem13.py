# problem 13

lines = []
with open ("problem13nums", "r") as f:
	for i in range(0, 100):
		lines.append(int(f.readline()))

first_10_digits_sum = sum(lines)
print(str(first_10_digits_sum)[0:10])
