# 최대 공약수 구하기
# a.주어진 수 모두의 약수인 정수
# b. input 2개 A,B
A,B = input("positive integers: ").split()
A= int(A)
B = int(B)
GCD=0
for i in range(1,min(A,B)):
	if A%i ==0 and B%i == 0:
		GCD = i
print("GCD is",GCD)
