t = int(input())
for i in range(t):
	r, s = input().split() #repeat number, string
	p = ""
	for i in s:
		p += i*int(r)
	print(p)
