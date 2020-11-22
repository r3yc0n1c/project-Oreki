#!/usr/bin/env python3
"""
Author:       r3yc0n1c
Date:         22 November 2020 (Sunday)
Description:  Bacon Cipher Decoder
				https://en.wikipedia.org/wiki/Bacon's_cipher#Cipher_details
"""
# Use only binary like data
def bacon_decode(cipher):
	# sanitize
	cipher = sanitize(cipher)

	print(f"[+] Cipher length: {len(cipher)}\n")
	alphs = [
			"ABCDEFGHIKLMNOPQRSTUWXYZ",
			"ABCDEFGHIKLMNOPQRSTVWXYZ",
			"ABCDEFGHJKLMNOPQRSTUWXYZ",
			"ABCDEFGHJKLMNOPQRSTVWXYZ",
			"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			]
	for a in alphs:				
		dec = ''
		for i in range(0, len(cipher), 5):
			try:
				chunk = cipher[i:i+5]
				idx = int(chunk, 2)
				dec += a[idx]
			except:
				print(f"[#] ERROR!!! Check the cipher again!!!")
				break
		print(f"[+] Decoded with {len(a)}-letter alphmap : {a}\n{dec}\n{dec.lower()}\n")

def sanitize(s):
	s = s.upper()
	chunk = s[:5]
	if 'A' in chunk and 'B' in chunk:
		s = s.replace('A', '0').replace('B', '1')
	s = s.replace(' ','')
	return s


def main():
	# test = "baaba aabbb aabaa abbbb baabb abaaa aaaba abaab aaaab baaaa abbab babaa abbaa aabab abbab babab abaaa baabb ababb abbba baaab abbab baabb aabaa baaaa baaba aabbb aabaa ababa aaaaa babbb babba aaabb abbab aabba"
	# test = "AABBBAABAAABABBABABBABBBABABBAABBBABAAABABABBAAABB"
	# test = "001011000000000011000001001000100010000100000000100110101100"
	test = "00001 00000 00010 01101 01100 10001 00010 01000 01110 00111 00100 10000 01101 10000 10010 00111 00100 00001 00000 00010 01101 01100 01000 00000 01100 00010 01000 01110 00111 00100 10000 01000 10001 00000 01011 00100 10010 00111 01101 00011 01101 00101 01011 00100 10001 10001 00000 00110 00100 00100 01100 00010 01101 00011 01000 01100 00110 00011 00100 10011 01000 10001 00100 00011 00001 10110 00101 10000 00000 01100 00010 01000 10001 00001 00000 00010 01101 01100"
	bacon_decode(test)

if __name__=='__main__':
	main()
