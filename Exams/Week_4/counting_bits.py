def countbits(n):
	a=[]
	b=0
	for i in range(n+1):
		c=bin(i)
		for j in c:
			if j == '1':
				b+=1
		a.append(b)
		b=0
	return a


print(countbits(15))
print(countbits(16))
print(countbits(1))
print(countbits(25))
print(countbits(5))
print(countbits(6))