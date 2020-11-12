A,B = input().split()
a,b = 0,0
for i in reversed(A):
	a = a*10+ int(i)
for i in reversed(B):
	b = b*10 + int(i)
print(max(a,b))
