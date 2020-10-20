#초ㅣ소고ㅇ배수 구하기
#a. 주어지ㄴ 수 모두으ㅣ 배수가 도ㅣ느ㄴ 저ㅇ수/다하ㅇ시ㄱ/호ㅏㄴ으ㅣ 우ㅓㄴ소
#b. input 2개 A,B
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
print(LCM)
