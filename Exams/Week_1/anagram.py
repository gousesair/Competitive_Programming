def check(s1, s2):
	# print(s1+"   "+s2)
	s1 = s1.replace(" ","")
	s2 = s2.replace(" ","")
	s1 = s1.lower()
	s2 = s2.lower()
	# print(s1+"   "+s2)
	if sorted(s1) == sorted(s2):
		print(True)
	else:
		print(False)
s1 ="Toss"
s2 ="Shot"
check(s1, s2)