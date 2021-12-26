# after bruteforcing failed, I just did this problem by hand. this code just served to check my answers

def import_data(filename):
	f = open(filename,'r')
	data = []
	d = []
	for line in f:
		if 'inp' in line:
			data.append(d)
			d = []
		d.append(line.strip().split())
	data.append(d)
	return data[1:]

def get_z(nstr):
	z = 0
	for i in range(len(nstr)):
		n = int(nstr[i])
		E = 1 - int(z%26 + B[i] == n)
		z = (25*E+1) * int(z/A[i]) + E*(n+C[i])
	return z

data = import_data('24-data')

A = [int(block[4][2]) for block in data]
B = [int(block[5][2]) for block in data]
C = [int(block[15][2]) for block in data]

print(get_z('12934998949199'))
print(get_z('11711691612189'))
	

#		x		y		z			w
#inp w		x0		y0		z0			n
#mul x 0	0		y0		z0			n
#add x z	z0		y0		z0			n
#mod x 26	z0%26		y0		z0			n
#div z A	z0%26		y0		z0/A			n
#add x B	z0%26 + B	y0		z0/A			n
#eql x w	D		y0		z0/A			n	D = int(z0%26 + B == n)
#eql x 0	E		y0		z0/A			n	E = not D	
#mul y 0	E		0		z0/A			n
#add y 25	E		25		z0/A			n
#mul y x	E		25*E		z0/A			n
#add y 1	E		25*E + 1	z0/A			n
#mul z y	E		25*E + 1	z0/A*(25E+1)		n
#mul y 0	E		0		z0/A*(25E+1)		n
#add y w	E		n		z0/A*(25E+1)		n
#add y C	E		n+C		z0/A*(25E+1)		n
#mul y x	E		E*(n+C)		z0/A*(25E+1)		n
#add z y	E		E*(n+C)		z0/A*(25E+1) + E*(n+C)	n
# z = (z0/A)*(25*E + 1) + E*(n+C)

# -----------
# treat z as base 26 number

# if E = 1 and A = 1	-> add digit n+C to the right
# if E = 0 and A = 1	-> don't do anything
# if E = 1 and A = 26	-> replace last digit by n+C
# if E = 0 and A = 26	-> remove last digit

# 1st digit: A=1, B=13, C=13
# E=1 ->			z = n0+13

# 2nd digit: A=1, B=11, C=10
# E=1 ->			z = n0+13,n1+10

# 3rd digit: A=1, B=15, C=5
# E=1 ->			z = n0+13,n1+10,n2+5

# 4th digit: A=26, B=-11, C=14
# E = 0 if n3 = n2 - 6 ->	z = n0+13,n1+10

# 5th digit: A=1, B=14, C=5
# E = 1 ->			z = n0+13,n1+10,n4+5

# 6th digit: A=26, B=0, C=15
# E = 0 if n5 = n4 + 5 ->	z = n0+13,n1+10

# 7th digit: A=1, B=12, C=4
# E = 1 ->			z = n0+13,n1+10,n6+4

# 8th digit: A=1, B=12, C=11
# E = 1 ->			z = n0+13,n1+10,n6+4,n7+11

# 9th digit: A=1, B=14, C=1
# E = 1 ->			z = n0+13,n1+10,n6+4,n7+11,n8+1

# 10th digit: A=26, B=-6, C=15
# E = 0 if n9 = n8 - 5 ->	z = n0+13,n1+10,n6+4,n7+11

# 11th digit: A=26, B=-10, C=12
# E = 0 if n10 = n7 + 1 ->	z = n0+13,n1+10,n6+4

# 12th digit: A=26, B=-12, C=8
# E = 0 if n11 = n6 - 8 ->	z = n0+13,n1+10

# 13th digit: A=26, B=-3, C=14
# E = 0 if n12 = n1 + 7 ->	z = n0+13

# 14th digit: A=26, B=-5, C=9
# E = 0 if n13 = n0 + 8 ->	z = 0

# n3 = n2 - 6
# n5 = n4 + 5
# n9 = n8 - 5
# n10 = n7 + 1
# n11 = n6 - 8
# n12 = n1 + 7
# n13 = n0 + 8

# big: 12934998949199
# small: 11711691612189
