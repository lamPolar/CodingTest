def ispossible(n, order):
	stack = []
	k = 1
	for i in order[:] :
		if i == n :
			stack.append(i)
			order.remove(i)
			n -= 1
		elif i == k:
			order.remove(i)
			k += 1
		else :
			stack.append(i)
			order.remove(i)
		while len(stack) and stack[-1] == k:
			stack.pop()
			k += 1
	if len(stack):
		return False
	return True


n = int(input())
order = list(map(int, input().split()))
if ispossible(n,order):
	print("Nice")
else:
	print("Sad")
