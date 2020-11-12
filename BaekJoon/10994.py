#recursion
"""
def star(n):
	if n==1:
		return ("*")
	else:
		return "*"*(4*n-3)+"\n*"+" "*(4*n-5)+"*\n"+"* "+star(n-1)+" *"+"\n*"+" "*(4*n-5)+"*\n"+"*"*(4*n-3)

print(star(3))

def star2(n):
	if n==1: return("*")
	else:
		return "*"*(4*n-3)+"\n* {} *\n".format(star2(n-1))+"*"*(4*n-3)
		
print(star2(3))
"""
def star3(n, result):
	#이차우ㅓㄴ 배여ㄹ 이요ㅇ

	pass
	
n = int(input())
result = [for i in range(n)]
print(result)
#result = star3(n,result)
#print(result)


