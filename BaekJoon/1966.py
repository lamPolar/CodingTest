import sys
def checkImportance(N, Q, I):
	check = 1
	while (len(I)):
		for item in I[:Q]:
			print("Q", Q)
			print(I)
			if item >= I[Q]:
				check += 1
				I.remove(item)
				Q -= 1
		print("Q2", Q)
		print("I2", I)
		if I.index(max(I)) > Q:
			maxI = I.index(max(I))
			for i in range(maxI):
				I.append(I.pop(0))
			Q = (Q + len(I) - maxI) % len(I)
		else:
			return (check)
			

T = int(sys.stdin.readline())
for i in range(T):
	N, Q = map(int, sys.stdin.readline().split())
	I = list(map(int, sys.stdin.readline().split()))
	result = checkImportance(N, Q, I)
	print(result)