n = 10
num1 = 0
num2 = 1
res = num2 
count = 1

while count <= n:
	print(res, end=" ")
	count += 1
	num1, num2 = num2, res
	res = num1 + num2
print()
