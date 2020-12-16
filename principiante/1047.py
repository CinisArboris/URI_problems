

def diferencia (inicio, fin, tipo):
	tope = -1
	if (tipo == 0):	tope = 24#0 = horas
	if (tipo == 1): tope = 60#1 = minutos
	dif = fin - inicio
	if (dif < 0): return dif * -1
	if (dif > 0): return dif
	if (dif == 0): return dif
	return -1
	
horas = 24
minutos = 60

hI = 7
mI = 0
hF = 8
mF = 0

hCiclo = -1
mCiclo = -1

dif = diferencia(mI, mF, 0)
if (dif == 60):
	hCiclo = dif
	print (hCiclo)
if (dif < 60):
	mCiclo = dif
	print (mCiclo)
	