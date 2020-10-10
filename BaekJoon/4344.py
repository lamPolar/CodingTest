C = int(input())
for i in range(C):
	n = input().split()
	sum = 0
	cnt = 0
	for j in range(1,len(n)):
		sum += int(n[j])
	avg = sum / int(n[0])
	for j in range(1,len(n)):
		if avg < int(n[j]):
			cnt +=1
	
	print(format((cnt/int(n[0])*100),".3f")+"%")
