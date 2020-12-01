# -*- coding: utf-8 -*-

numero_empleado = int(input())
numero_hrs_mes = int(input())
pago_por_hora = float('%.2f' % ( float(input()) ))

pago_por_mes = pago_por_hora*numero_hrs_mes
pago_por_mes = '%.2f'%(float(pago_por_mes))

print ("NUMBER = " + str(numero_empleado))
print ("SALARY = U$ " + str(pago_por_mes))