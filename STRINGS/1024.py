# -*- coding: utf-8 -*-
import math

# -------------------------------------------------
def codificar(cadena, posiciones, orientacion, codigo):
	# [orientacion] == 0 , derecha
	# [orientacion] == 1 , izquierda
	resultado = ''
	for cadA in cadena:
		if (
			((ord(cadA) >= ord('a')) and (ord(cadA) <= ord('o')))
			or
			((ord(cadA) >= ord('p')) and (ord(cadA) <= ord('z')))
			or
			((ord(cadA) >= ord('A')) and (ord(cadA) <= ord('O')))
			or
			((ord(cadA) >= ord('P')) and (ord(cadA) <= ord('Z')))
			or
			codigo
		):
			varA = cadA			#string
			varB = ord(cadA)	#decimal
			varC = chr(varB)	#string
			if (orientacion == 0): varB = varB + posiciones	#decimal +3
			if (orientacion == 1): varB = varB - posiciones	#decimal +3
			varA = chr(varB)	#string +3
			resultado = resultado + varA
		else:
			resultado = resultado + cadA
	return resultado
# -------------------------------------------------
def parte_01(cadena):
	# cada letra mayúscula o minúscula
	# debe desplazarse tres posiciones hacia la derecha
	resultado = codificar(cadena, 3, 0, False)
	
	# invertirse
	resultado = resultado[::-1]
	
	
	mitad = int(len(resultado)/2)
	p1 = resultado[:mitad]
	p2 = resultado[mitad:]
	# la mitad en adelante (truncado)
	# deben moverse una posición a la izquierda
	p2 = codificar(p2, 1, 1, True)
	
	resultado = p1+p2
	return resultado
# **************************************************
# ******************  M  A  I  N
inicINPUT = 1
topeINPUT = int(math.pow(10,4))

entrINPUT = int(input())
if (entrINPUT < inicINPUT): exit()
if (entrINPUT > topeINPUT): exit()

inicSTR = 1
topeSTR = int(math.pow(10,3))
listaLINEAS = []
for a in range(entrINPUT):
	entrSTR = input()
	if (len(entrSTR) < inicINPUT): exit()
	if (len(entrSTR) > topeINPUT): exit()
	listaLINEAS.append(entrSTR)

listaCOD = []
for linea in listaLINEAS:
	print (parte_01(linea))


