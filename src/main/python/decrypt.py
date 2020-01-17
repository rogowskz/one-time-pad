f = open("src/test/data/ciphertext.1.txt", 'r')
file = f.read()
lines = file.split('\n')
binaries = []
for x in lines:
	if x!='': binaries.append(bin(int(x, 16))[2:])
base = str(binaries[0])
binaries.pop(0)

for y in binaries:
	result=''
	x = 0
	while x<len(y):
		try:
			if str(y[x])==str(base[x]):
				result+="0"
			else:
				result+="1"
		except:
			try:
				if str(base[x])=="0":
					result+="0"
				else: result+="1"
			except:
				if str(y[x])=="0":
					result+="0"
				else: result+="1"
		x+=1
	base = str(result)
print(base)
