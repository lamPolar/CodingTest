import sys

num = int(input())
stack = []
for i in range(num):
	cmd = sys.stdin.readline().split()
	if cmd[0] == 'push':
		stack.append(int(cmd[1]))
	elif cmd[0] == "top":
		if (len(stack)):
			print(stack[-1])
		else :
			print(-1)
	elif cmd[0] == "size":
		print(len(stack))
	elif cmd[0] == "empty":
		if len(stack):
			print(0)
		else:
			print(1)
	elif cmd[0] == "pop":
		if len(stack):
			print(stack.pop())
		else :
			print(-1)