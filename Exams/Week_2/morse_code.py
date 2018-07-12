dicta = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

x=""
z=[]
y=[]
def conversion(a):
	global x
	global z
	for i in a:
		for j in range(len(i)):
			y=dicta[str(i[j])]
			x=x+y
		# print(x)
		z.append(x)
		x=""
	return z

def transformations(b):
	global y
	for i in b:
		if i not in y:
			y.append(i)
	return len(y)


# conversion(["bhi","vsv","sgh","vbi"])
print(transformations(conversion(["bhi","vsv","sgh","vbi"])))