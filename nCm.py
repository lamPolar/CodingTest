#순열과 조합
#array n, number m이 주어짐
# nCm, nPm?
#nPr = (n)!/(n-r)!
#nCr = nPr/r! = n!/((n-r)!*r!)
#combination
n = input("input array:").split()
r = int(input("positive integer:"))
def Per(n,r):
	result = 1
	for i in range(1,len(n)+1):
		result = result * i
	for j in range(1,len(n)+1-r):
		result = result / j
	print("nPr = ",int(result))
def Com(n,r):
	result = 1
	for i in range(1,len(n)+1):
		result = result*i
	for j in range(1,len(n)+1-r):
		result = result/j
	for k in range(1,r+1):
		result = result/k
	print("nCr = ",int(result))
Per(n,r)
Com(n,r)
