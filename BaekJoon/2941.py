s = input() 
result = []
i = 0
while i < len(s):
	if s[i:i+2] == "c=":
		i += 2
		result.append("c=")
		continue
	if s[i:i+2] == "c-":
		i += 2
		result.append("c-")
		continue
	if s[i:i+3] == "dz=":
		i += 3
		result.append("dz=")
		continue
	if s[i:i+2] == "d-":
		i += 2
		result.append("d-")
		continue
	if s[i:i+2] == "lj":
		i += 2
		result.append("lj")
		continue
	if s[i:i+2] == "nj":
		i+=2
		result.append("nj")
		continue
	if s[i:i+2] == "s=":
		i+=2
		result.append("s=")
		continue
	if s[i:i+2] == "z=":
		i+=2
		result.append("z=")
		continue
	else:
		result.append(s[i])
		i+=1
print(result)
print(len(result))

