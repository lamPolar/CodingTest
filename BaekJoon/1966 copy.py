import sys
def checkImportance(N, Q, I):
	check = 1
	newQ = Q
	point = newQ
	for item in I[:]:
		if item < I[newQ]:
			if I.index(item) < newQ:
				newQ -= 1
			I.remove(item)
	for item in I[:]:
		if (item > I[newQ]):
			if I.index(item) < newQ:
				newQ -= 1
			check += 1
			point = I.index(item)
			I.remove(item)
	if len(I) == 1 or point == newQ:
		return (check)
	elif point < newQ:
		check += newQ - point
		return (check)
	elif point > newQ:
		check += len(I) - point + newQ
		return (check)

T = int(sys.stdin.readline())
for i in range(T):
	N, Q = map(int, sys.stdin.readline().split())
	I = list(map(int, sys.stdin.readline().split()))
	result = checkImportance(N, Q, I)
	print(result)