#!/usr/bin/env python3
"""
Author:       r3yc0n1c
Date:         10 November 2020 (Tuesday)
Description:  Base 3 (0, 1, 2) A1Z26 (a=1, z=26, ' '=27, '_'=28) decoder
"""
cipher = "22 12 200 12 1000 212 12 1000 210 201 12 1000 202 12 200 112 1 200 221 1000 202 120 1000 21 12 202 1000 202 22 12 1000 20 110 1 21 1000 202 22 200 12 12 1001 11 100 21 100 202 201 1001 100 201 112 202 1001 211 12 200 221 1001 201 12 10 210 200 12"

dec = ""
for n in cipher.split(' '):
	num = int(n, 3)
	if num==27:
		dec += ' '
	elif num==28:
		dec += '_'
	else:
		dec += chr(ord('a')-1 + num)
print(f"# Result:\n{dec}")
