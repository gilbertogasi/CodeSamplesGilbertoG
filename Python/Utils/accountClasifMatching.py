# -*- coding: utf-8 -*-

##########################################################################################################################
##
## Author: Gilberto Guerrero
## Date: 25/05/2020
## Comment: Script para automatizar la busqueda de caracteres especiales en nombre de ciudades.
## Version: 1.01
##
##########################################################################################################################

file1 = 'c:\\temp\\Copia de B11 - ABRIL 2020 COVID - 19 (1).xlsx' # path to file + file name
file2 = 'c:\\temp\\Copia de Plantilla de cuentas nuevas del covid 19 para abril 30 2020 (00.._.xls' # path to file + file name
sheetf1 = 'B11 ABRIL 2020' # sheet name or sheet number or list of sheet numbers and names
sheetf2 = 'CATALOGO DE CUENTAS' # sheet name or sheet number or list of sheet numbers and names

Clasif = None
CtaCont = ''

Nivel1 = []
Nivel2 = []
Nivel3 = []
Nivel7 = []
Descripcion = []
ClaseCta = []
Renglon = []
DescClas = []

import pandas as pd

df1 = pd.read_excel(io=file1, sheet_name=sheetf1)
df2 = pd.read_excel(io=file2, sheet_name=sheetf2)

for i in df1.index:
    CtaCont = str(df1['CUENTA CONTABLE'][i])

    for j in df2.index:
        Clasif = str(df2['NIVEL1'][j]) + str(df2['NIVEL2'][j])

        if CtaCont[0:6:] == Clasif:
            Nivel1.append(df2['NIVEL1'][j])
            Nivel2.append(df2['NIVEL2'][j])
            Nivel3.append(df2['NIVEL3'][j])
            Nivel7.append(df2['NIVEL7'][j])
            Descripcion.append(df2['DESCRIPCIÓN'][j])
            ClaseCta.append(df2['CLASE CUENTA'][j])
            Renglon.append(df1['RENGLON'][i])
            DescClas.append(df1['CUENTA CONTABLE'][i])

df = pd.DataFrame({'NIVEL_1': Nivel1,
                   'NIVEL_2': Nivel2,
                   'NIVEL_3': Nivel3,
                   'NIVEL_7': Nivel7,
                   'DESCRIPCION': Descripcion,
                   'CLASE_CUENTA': ClaseCta,
                   'RENGLON': Renglon,
                   'DESCRIP_CLASIF': DescClas})

writer = pd.ExcelWriter('c:\\temp\\MacheoClasifCont.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()