n = int(input())
result = 0
if n<100:
	result += n
else:
	result += 99
for i in range(100,n+1):
	diff1 = i//100
	diff2 = (i % 100)//10
	diff3 = (i % 100)%10
	if diff1-diff2 == diff2-diff3:
		result+=1

print(result)
	
	
	
	
