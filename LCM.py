# 최소공배수 구하기
# a.주어진 수 모두의 배수가 되는 정수
#다항식, 환??
# b. input 2개 A,B
A, B = input().split()
A = int(A)
B = int(B)
m = max(A,B)
n = min(A,B)
i = 1
LCM = 0
while True:
	mul = m*i
	if mul % n == 0:
		LCM = mul
		break
	i+=1
print("LCM is", LCM)
