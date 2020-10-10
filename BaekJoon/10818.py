n= int(input())
mlist = input().split()
for i in range(n):
	mlist[i] = int(mlist[i])
print(min(mlist), max(mlist))
