s = input() 
result, i= 0,0
while i < len(s):
	if s[i:i+2] == "c=":
		i += 2
	elif s[i:i+2] == "c-":
		i += 2
	elif s[i:i+3] == "dz=":
		i += 3
	elif s[i:i+2] == "d-":
		i += 2
	elif s[i:i+2] == "lj":
		i += 2
	elif s[i:i+2] == "nj":
		i+=2
	elif s[i:i+2] == "s=":
		i+=2
	elif s[i:i+2] == "z=":
		i+=2
	else:
		i+=1
	result+=1
    
print(result)
