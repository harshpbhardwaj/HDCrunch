la = int(input("Enter password length limit min "))
lb = int(input("Enter password length limit max "))
ln = la - lb

nwords = int(input("How many words you have "))
allstr = [""]
for x in range(0,nwords):
	allstr.append(str(input("Enter the word ")))
allstr.pop(0)
word = [""]
l = la
while (l<=lb):
	for strg in allstr:
		n = l - len(strg)
		p = int(pow(10,n))
		for m in range(0,p):
			a = len(str(m))
			word.append(strg)
			for x in range(0,n-a):
				word.append(str(0))
			word.append(str(m) + "\n")
		for m in range(0,p):
			a = len(str(m))
			for x in range(0,n-a):
				word.append(str(0))
			word.append(str(m) + strg + "\n")
		for m in range(0,p):
			a = len(str(m))
			if a>(n-1):
				continue
			for x in range(0,n-(a+1)):
				word.append(str(0))
			word.append(str(m))
			word.append("@" + strg + "\n")
		for m in range(0,p):
			a = len(str(m))
			if a>(n-1):
				continue
			for x in range(0,n-(a+1)):
				word.append(str(0))
			word.append(strg)
			word.append("@" + str(m) + "\n")
	for strg in allstr:
		n = l - len(strg)
		p = int(pow(10,n))
		for m in range(0,p):
			a = len(str(m))
			word.append(strg.capitalize())
			for x in range(0,n-a):
				word.append(str(0))
			word.append(str(m) + "\n")
		for m in range(0,p):
			a = len(str(m))
			for x in range(0,n-a):
				word.append(str(0))
			word.append(str(m) + strg.capitalize() + "\n")
		for m in range(0,p):
			a = len(str(m))
			if a>(n-1):
				continue
			for x in range(0,n-(a+1)):
				word.append(str(0))
			word.append(str(m))
			word.append("@" + strg.capitalize() + "\n")
		for m in range(0,p):
			a = len(str(m))
			if a>(n-1):
				continue
			for x in range(0,n-(a+1)):
				word.append(str(0))
			word.append(strg.capitalize())
			word.append("@" + str(m) + "\n")
	l += 1


f = open("dict.txt", "w")
for w in word:
	f.write(w)


f.close()