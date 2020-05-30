# -*- coding: utf-8 -*-

##########################################################################################################################
##
## Author: Gilberto Guerrero
## Date: 20/05/2020
## Comment: Script para automatizar la generacion de secuencias para archivos Excel de Sistemas Geopoliticos para Abanks
## Version: 1.00
##
##########################################################################################################################

file_name = 'c:\\temp\\Nivel III-Ciudad-municipio-capital existentes (ver 2).xlsx' # path to file + file name
sheet = 'Municipios' # sheet name or sheet number or list of sheet numbers and names

import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=sheet)

PAIEX = [248,60,136,184,234,238,580,584,90,796,92,850,876,376,380,434,388,392,832,400,634,398,404,417,296,414,418,
         426,428,422,430,438,440,170,174,178,442,446,807,450,458,454,462,466,470,504,474,480,478,175,583,492,496,
         499,500,508,104,516,520,524,558,562,566,570,578,540,554,512,528,586,585,598,600,604,612,258,616,620,630,
         826,760,140,203,408,498,214,156,638,646,642,732,882,16,652,659,674,663,666,670,654,662,336,678,686,688,
         690,694,702,706,144,710,736,752,756,740,744,748,764,158,834,762,86,275,260,304,626,772,776,780,788,795,
         792,798,804,800,858,860,548,704,334,887,4,8,276,20,24,660,10,28,530,682,12,32,51,533,36,40,31,44,48,50,
         52,56,84,204,112,68,70,72,76,96,100,854,108,64,132,116,120,124,148,152,196,166,180,410,384,188,191,192,
         208,212,218,818,222,784,703,705,581,233,231,643,242,608,246,250,249,266,270,268,239,288,292,308,300,312,
         316,320,328,254,831,324,624,226,332,340,344,348,356,360,768,368,364,372,74,833,162,574,352]
DEPEX = 99

Pais = 0
Depto = 0
Muni = 0
Seq = []
conteo = 0

for i in df.index:
    if Pais != df['CODIGO_PAIS'][i]:
        Pais = df['CODIGO_PAIS'][i]
        Depto = df['CODIGO_DEPARTAMENTO'][i]
        Muni = 1
    else:
        if Depto != df['CODIGO_DEPARTAMENTO'][i]:
            Depto = df['CODIGO_DEPARTAMENTO'][i]
            if Pais in PAIEX and Depto == DEPEX and conteo == 0:
                Muni = 999
                conteo += 1
            else:
                Muni = 1
        else:
            conteo = 0
            if Muni == 999:
               Muni = 1
            else:
               Muni += 1

    Seq.append(Muni)

df = pd.DataFrame({'CODIGO_MUNICIPIO': Seq})
writer = pd.ExcelWriter('c:\\temp\\demo.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()