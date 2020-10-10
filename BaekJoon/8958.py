n = int(input())
A = []
B =[]
for i in range(n):
	A.append(input())
for i in A:
	cnt = 0
	sum = 0
	for j in range(len(i)):
		if i[j] == "O":
			cnt += 1
			sum += cnt 						
		else :
			cnt = 0
	B.append(sum)
for i in range(len(B)):
	print(B[i])
