n = int(input()) #number of words
words, groups = [],0
for i in range(n):
	words.append(input())
for i in words:
	used = []
	before = ""
	isGroup = True
	for j in i:
		if j not in used:
			used.append(j)
			before = j
		else:
			if j != before:
				isGroup = False
	if isGroup == True:
		groups+=1

print(groups)
