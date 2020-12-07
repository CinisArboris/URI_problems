# -*- coding: utf-8 -*-
porce = 0.15

nombr = str(input())
salar = float(input())
venta = float(input())
comis = venta * porce
netos = round(salar + comis, 2)
print ('TOTAL = R$', '%.2f'%netos)