from collections import Counter
s = input().lower() #letters
"""
used = {}
for i in s:
	if i in used:
		used[i]+=1
	else:
		used[i]=1
"""
used = Counter(s)
new = used.most_common(2)

"""
new = sorted(used.items(), key = lambda x:x[1], reverse = True)[:2]
"""
if len(new)==1 or new[0][1]!= new[1][1]:
	print(new[0][0].upper())
else:
	print("?")
	
