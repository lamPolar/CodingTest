import string
s = input() #letters
#a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b = list(string.ascii_lowercase)
for i in b:
	if i in s:
		print(s.index(i),end =" ")
	else:
		print(-1, end = " ")		

