# -*- coding: utf-8 -*-

dix = {'bonecos':8,'arquitetos':4,'musicos':6,'desenhistas':12}

Vbon = []
Varq = []
Vmus = []
Vdes = []

minDuendes = 1
maxDuendes = 1000
minHoras = 1
maxHoras = 24

duendes = int(input())
if (duendes < minDuendes): exit()
if (duendes > maxDuendes): exit()

for du in range(duendes):
	E, G, H = map(str, input().split())
	
	if (G not in dix): exit()
	if (H.isnumeric() == False): exit()
	
	H = int(H)
	if (H < minHoras): exit()
	if (H > maxHoras): exit()
	
	if (G == 'bonecos'):
		Vbon.append(H)	
	if (G == 'arquitetos'):
		Varq.append(H)
	if (G == 'musicos'):
		Vmus.append(H)
	if (G == 'desenhistas'):
		Vdes.append(H)

Vbon = int(sum(Vbon) / dix['bonecos'])
Varq = int(sum(Varq) / dix['arquitetos'])
Vmus = int(sum(Vmus) / dix['musicos'])
Vdes = int(sum(Vdes) / dix['desenhistas'])

print (Vbon + Varq + Vmus + Vdes)