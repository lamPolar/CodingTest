n = int(input())
#고ㅏ모ㄱ 개수
score = input().split()
for i in range(n):
	score[i] = int(score[i])
m = max(score)
sum = 0
for i in range(n):
	sum += score[i]/m*100
print(sum/n)

