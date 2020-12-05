# -*- coding: utf-8 -*-

def parte_01():
	cadena = '!@#$'
	resultado = ''
	#cad_str = cadena
	#cad_hex = hex(ord(cad_str))		#string		| str
	#cad_bin = bin(ord(cad_str))		#str > bin  | str
	#cad_ord = ord(cad_str)			#str > int  | int
	
	
	for cadA in cadena:
		varA = cadA			#string
		varB = ord(cadA)	#decimal
		varC = chr(varB)	#string
		print(varA, varB, varC)
		print ('-'*10)
		varB = varB + 3		#decimal +3
		varA = chr(varB)	#string +3
		print ('>', varB, varA)
		print ('*'*10)
	#print ('antes' , cadena)
	#print ('string     ', cad_str)
	#print ('hexadecimal', cad_hex)
	#print ('binario    ', cad_bin)
	#print ('decimal    ', cad_ord)
	
	#print ('*****')
	#for let in cadena:
	#	resultado = resultado + str((ord(let) + 3))
	#print ('resultado', resultado)
	return resultado


def parte_02(cadena):
	return cadena

# **************************************************
# ******************  M  A  I  N
resultado = parte_02(parte_01())
