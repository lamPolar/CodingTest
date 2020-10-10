num1 = int(input())
num2 = int(input())
num3 = int(input())
mul = str(num1*num2*num3)
cnt = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(mul)):
	cnt[int(mul[i])] +=1
for i in range(len(cnt)):
	print(cnt[i])
