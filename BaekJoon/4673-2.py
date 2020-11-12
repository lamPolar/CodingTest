def d(n):
	tmp = n
	while tmp != 0:
		n += tmp%10
		tmp = tmp//10
	return n

array = []
for i in list(range(1,10001)):
	array.append(d(i))	
	if i not in array:
		print(i)

