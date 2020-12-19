# -*- coding: utf-8 -*-
esferTeori = -1

minEsfer = 1
maxEsfer = 1000

minRamas = 100
maxRamas = 1000

cajonEsfer = int(input())
if (cajonEsfer < minEsfer): exit(1)
if (cajonEsfer > maxEsfer): exit(1)

cajonRamas = int(input())
if (cajonRamas < minRamas): exit(1)
if (cajonRamas > maxRamas): exit(1)


if ((cajonRamas%2) != 0):
	cajonRamas = cajonRamas - 1

esferTeori = int(cajonRamas / 2) * -1
faltaEsfer = cajonEsfer + esferTeori

if (faltaEsfer < 0):
	print ('Faltam', faltaEsfer*-1, 'bolinha(s)')
else:
	print ('Amelia tem todas bolinhas!')