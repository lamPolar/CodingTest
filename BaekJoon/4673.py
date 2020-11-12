def d(n):
	tmp = n
	while tmp != 0:
		n += tmp%10
		tmp = tmp//10
	return n


def selfnum(n):
	result = []
	looked = []
	for i in range(1,n+1):
		if i not in looked:
			result.append(i)
			k = i
			while k <= n:
				k = d(k)
				looked.append(k)
			
	return result

final = selfnum(10000)
for i in final:
	print(i)
	

