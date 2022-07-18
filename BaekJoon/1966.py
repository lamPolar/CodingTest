import sys
def checkImportance(N, Q, I):
	check = 0
	while I:
		if I[0] == max(I):
			check += 1
			if Q == 0:#찾고싶었던 Q라면
				return check
			I.pop(0)
			Q -= 1	
		else :
			I.append(I.pop(0))
			if Q == 0:
				Q += len(I)
			Q -= 1
T = int(sys.stdin.readline())
for i in range(T):
	N, Q = map(int, sys.stdin.readline().split())
	I = list(map(int, sys.stdin.readline().split()))
	result = checkImportance(N, Q, I)
	print(result)