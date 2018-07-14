def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

print("Testcase1")
a = "{0:08b}".format(25)
b = "{0:08b}".format(30)
print(hamming(str(a),str(b)))
print("\n")

print("Testcase2")
a = "{0:08b}".format(1)
b = "{0:08b}".format(4)
print(hamming(str(a),str(b)))
print("\n")

print("Testcase3")
a = "{0:09b}".format(100)
b = "{0:09b}".format(250)
print(hamming(str(a),str(b)))
print("\n")

print("Testcase4")
a = "{0:08b}".format(1)
b = "{0:08b}".format(30)
print(hamming(str(a),str(b)))
print("\n")

print("Testcase5")
a = "{0:09b}".format(255)
b = "{0:09b}".format(0)
print(hamming(str(a),str(b)))
print("\n")
