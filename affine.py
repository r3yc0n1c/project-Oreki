#!/usr/bin/env python3
# pip3 install pycryptodome
from Crypto.Util.number import inverse

lookup = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6,
	'H': 7,
	'I': 8,
	'J': 9,
	'K': 10,
	'L': 11,
	'M': 12,
	'N': 13,
	'O': 14,
	'P': 15,
	'Q': 16,
	'R': 17,
	'S': 18,
	'T': 19,
	'U': 20,
	'V': 21,
	'W': 22,
	'X': 23,
	'Y': 24,
	'Z': 25
}

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def encrypt(text, a, b):
	# y = E(x) = (ax + b) mod 26
	
	enc = ''
	for x in text:
		if x in lookup:
			enc += get_key( (a*lookup[x] + b) % 26 )
		else:
			enc += x
	return enc

def decrypt(text, a, b):
	# x = movinv(a, 26) * (y-b) % 26

	dec = ''
	for y in text:
		if y in lookup:
			dec += get_key( inverse(a, 26)*(lookup[y] - b) % 26 )
		else:
			dec += y
	return dec

def test():
	m = 'FLAG{TESTING_AFFINE}'
	c = encrypt(m, 5, 8)
	print(c)
	print(decrypt(c, 5, 8))

# Brute-force all possible solutions
def affine_BF(c):
	for a in range(26):
		for b in range(26):
			print(f"[a:{a}, b:{b}]> {decrypt(c, a, b)}")

if __name__ == '__main__':
	# test()
	c = 'HLIM{ZCUZWVM_IHHWVC}'
	c = c.upper()

	affine_BF(c)