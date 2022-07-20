import sys
def checkImportance(N, Q, I):
	check = 1
	point = 0
	for item in I[:]:
		if item < I[Q]:
			if I.index(item) < Q:
				Q -= 1
			I.remove(item)
	for item in I[:]:
		if item > I[Q]:
			if I.index(item) < Q:
				Q -= 1
			check += 1
			point = I.index(item) % (len(I) - 1)
			I.remove(item)
	if point < Q:
		check += Q - point
	elif point > Q:
		check += len(I) - point + Q
	return(check)

T = int(sys.stdin.readline())
for i in range(T):
	N, Q = map(int, sys.stdin.readline().split())
	I = list(map(int, sys.stdin.readline().split()))
	print(checkImportance(N, Q, I))
