from fractions import gcd
print("Value A is the numerator and B is the denominator")
a = (input("A:"))
b = (input("B:"))
c = int(a)
d = int(b)
gcd = gcd(c,d)
e = str(int(c / gcd))
f = str(int(d / gcd))
print("The fraction " + a + "/" + b + " equals " + e + "/" + f)
