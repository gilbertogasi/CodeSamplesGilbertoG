# -*- coding: utf-8 -*-

##########################################################################################################################
##
## Author: Gilberto Guerrero
## Date: 25/05/2020
## Comment: Script para automatizar la busqueda de caracteres especiales en nombre de ciudades.
## Version: 1.01
##
##########################################################################################################################

file_name = 'c:\\temp\\Nivel III-Ciudad-municipio-capital existentes (ver 2).xlsx' # path to file + file name
sheet = 'Municipios' # sheet name or sheet number or list of sheet numbers and names
patron = r'[^"a-z" "A-Z" "0-9" "[" .()-/]'
Pais = []
Dept = []
Muni = []
Nombre = []

import pandas as pd
import re
df = pd.read_excel(io=file_name, sheet_name=sheet)

for i in df.index:
    if re.search(patron, df['NOMBRE_CIUDAD'][i]):
        Pais.append(df['CODIGO_PAIS'][i])
        Dept.append(df['CODIGO_DEPARTAMENTO'][i])
        Muni.append(df['CODIGO_MUNICIPIO'][i])
        Nombre.append(df['NOMBRE_CIUDAD'][i])

df = pd.DataFrame({'CODIGO_PAIS': Pais, 'CODIGO_DEPARTAMENTO': Dept, 'CODIGO_MUNICIPIO': Muni, 'NOMBRE_CIUDAD': Nombre})
writer = pd.ExcelWriter('c:\\temp\\EspecialCharCiudades.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()