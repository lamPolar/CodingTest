A =[]
for i in range(10):
	A.append(int(input())%42)
B =[]
for i in A:
	if i not in B:
		B.append(i)
print(len(B))
"""
#using set

A =[]
for i in range(10):
	A.append(int(input())%42)
B = set(A)
print(len(B))
"""
