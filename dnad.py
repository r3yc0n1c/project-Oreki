#!/usr/bin/env python3
import math

"""
Author:       r3yc0n1c
Date:         13 November 2020 (Friday)
Description:  DNA Cryptography Decryption Tool
"""

def sanitize(raw):
	s = 'ATCG'
	clean = raw
	junk = []
	for i in range(len(raw)):
		if raw[i] not in s:
			junk.append([raw[i], i])
			clean = clean.replace(raw[i], '')
	return clean, junk

"""
---------------
DNA-Crypt Algo
---------------
https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-176
https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-176/tables/1
"""
def DNACrypt(cipher):
	codon_ascii = {
	'CGA' : 'A',
	'CCA' : 'B',
	'GTT' : 'C',
	'TTG' : 'D',
	'GGC' : 'E',
	'GGT' : 'F',
	'TTT' : 'G',
	'CGC' : 'H',
	'ATG' : 'I',
	'AGT' : 'J',
	'AAG' : 'K',
	'TGC' : 'L',
	'TCC' : 'M',
	'TCT' : 'N',
	'GGA' : 'O',
	'GTG' : 'P',
	'AAC' : 'Q',
	'TCA' : 'R',
	'ACG' : 'S',
	'TTC' : 'T',
	'CTG' : 'U',
	'CCT' : 'V',
	'CCG' : 'W',
	'CTA' : 'X',
	'AAA' : 'Y',
	'CTT' : 'Z',
	'ACT' : '0',
	'ACC' : '1',
	'TAG' : '2',
	'GCA' : '3',
	'GAG' : '4',
	'AGA' : '5',
	'TTA' : '6',
	'ACA' : '7',
	'AGG' : '8',
	'GCG' : '9',
	'ATA' : ' ',
	'TCG' : ',',
	'GAT' : '.',
	'GCT' : ':'
	}
	
	print(f"\n[+] Cipher:\n{cipher}")
	
	clean, junk = sanitize(cipher)	
	print(f"\n[+] Clean Sequence:\n{clean}")
	
	print("\n[+] Junk(s):")
	for j in junk:
		print(j)

	assert len(clean)%3 == 0, "Length is not a multiple of 3 !!!"

	decoded = ''
	for i in range(0, len(clean), 3):
		chunk = clean[i:i+3]
		decoded += codon_ascii[chunk]
	print(f"\n[+] Decoded:\n{decoded}")

	# add junks
	for j in junk:
		left = decoded[:math.ceil(j[1]/3)]
		right = decoded[math.ceil(j[1]/3):]
		decoded = left + j[0] + right
	print(f"\n[+] Decoded with junks:\n{decoded}")

"""
Binary Data to DNA Sequence
"""
def bin2DNA(data):
	assert len(data)%2 == 0, "Length must be a multiple of 2 !!!"
	
	bin_dna = {
    '00' : 'A',
    '10' : 'C',
    '01' : 'G',
    '11' : 'T'
	}

	codon_seq = ''
	for i in range(0, len(data), 2):
		chunk = data[i:i+2]
		codon_seq += bin_dna[chunk]
	return codon_seq

"""
DNA Algo
"""
def DNA(cipher):
	codon_ascii = {
    'AAA' : 'a',
    'AAC' : 'b',
    'AAG' : 'c',
    'AAT' : 'd',
    'ACA' : 'e',
    'ACC' : 'f',
    'ACG' : 'g',
    'ACT' : 'h',
    'AGA' : 'i',
    'AGC' : 'j',
    'AGG' : 'k',
    'AGT' : 'l',
    'ATA' : 'm',
    'ATC' : 'n',
    'ATG' : 'o',
    'ATT' : 'p',
    'CAA' : 'q',
    'CAC' : 'r',
    'CAG' : 's',
    'CAT' : 't',
    'CCA' : 'u',
    'CCC' : 'v',
    'CCG' : 'w',
    'CCT' : 'x',
    'CGA' : 'y',
    'CGC' : 'z',
    'CGG' : 'A',
    'CGT' : 'B',
    'CTA' : 'C',
    'CTC' : 'D',
    'CTG' : 'E',
    'CTT' : 'F',
    'GAA' : 'G',
    'GAC' : 'H',
    'GAG' : 'I',
    'GAT' : 'J',
    'GCA' : 'K',
    'GCC' : 'L',
    'GCG' : 'M',
    'GCT' : 'N',
    'GGA' : 'O',
    'GGC' : 'P',
    'GGG' : 'Q',
    'GGT' : 'R',
    'GTA' : 'S',
    'GTC' : 'T',
    'GTG' : 'U',
    'GTT' : 'V',
    'TAA' : 'W',
    'TAC' : 'X',
    'TAG' : 'Y',
    'TAT' : 'Z',
    'TCA' : '1',
    'TCC' : '2',
    'TCG' : '3',
    'TCT' : '4',
    'TGA' : '5',
    'TGC' : '6',
    'TGG' : '7',
    'TGT' : '8',
    'TTA' : '9',
    'TTC' : '0',
    'TTG' : ' ',
    'TTT' : '.'
	}

	print(f"\n[+] Cipher:\n{cipher}")

	decoded = ''
	for i in range(0, len(cipher), 3):
		chunk = cipher[i:i+3]
		decoded += codon_ascii[chunk]
	print(f"\n[+] Decoded:\n{decoded}")


def main():
	cipher = "GTTAAAGTTTTCGGT{ACGACTTGCCCTACCTCTTTTATAGTGTCAACTAGGTGCGCATCCAGAATAACCACGATAACCTCTATAAAAACTCTGTCAATATTGTCTCGA}"
	DNACrypt(cipher)
	"""
	cipher.txt
	--------------
	0100 0100 1110
	...
	...
	...
	0011 1111 11
	--------------
	"""
	cipher = bin2DNA(open('./cipher.txt','r').read().replace(' ','').replace('\n',''))
	DNA(cipher)

if __name__ == "__main__":
	main()
