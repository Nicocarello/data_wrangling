import pandas as pd


data = pd.read_csv("D:/Anaconda/datasets/customer-churn-model/Customer Churn Model.csv")

print(data)
print()
print()


#CREAR SUBCONJUNTO DE DATOS######

#CREAR SUBCONJUNTO DE UNA COLUMNA
account_length = data['Account Length']

print(account_length)
print()
print()

#CREAR UN DATAFRAME CON VARIAS COLUMNAS DEL CSV
subset = data[['Account Length','Phone','Eve Charge','Day Calls']]

print(subset)
print()
print()

#CREAR UNA LISTA CON LAS COLUMNAS QUE QUERES
desired_columns = ['Account Length','Phone','Eve Charges','Day Calls']

#TOTAL DE LAS COLUMNAS
all_columns_list = data.columns.values.tolist()

#RECORRO CON EL FOR TODAS LAS COLUMNAS Y GUARDO SOLO LAS QUE QUIERO TABAJAR

sublist = [x for x in all_columns_list if x in desired_columns]

print(sublist)
#CREO UN DATAFRAME CON LAS LISTAS DESEADAS

data2 = data[sublist]

print(data2)
print()
print()

#PRINTEO LAS PRIMERAS 25 COLUMNAS
print(data[0:25])

#FILTRO POR LAS QUE TIENEN TOTAL MINS MENOR A 200
data1 = data[data['Day Mins']>200]

print(data1)

#USUARIOS QUE SON DE NUEVA YORK

data2 = data[data['State']=='NY']

print(data2)

#FILTRO CON MAS DE UNA CONDICION AND

data3 = data[(data['Day Mins']>300) & (data['State']=='NY')]

print(data3)

#FILTRO CON UNA CONDICION OR

data4 = data[(data['Day Mins']>300) | (data['State']=='NY')]

print(data4)

#MINUTOS DE DIA, DE NOCHE Y LONGITUD DE LA CUENTA DE LOS PRIMEROS 50

subset_first_50 = data[['Day Mins','Night Mins','Account Length']][:50]
print(subset_first_50)

#PRINTEO LAS PRIMERAS 10 FILAS Y DE LA 3 A LA 6 COLUMNAS

print(data.iloc[1:10,3:6])

#TODAS LAS FILAS DE LA COLUMNAS 3 A 6
print(data.iloc[:,3:6])

#TODAS LAS COLUMNAS PARA LAS FILAS 1 A 10

print(data.iloc[1:10,:])

#CREO UNA NUEVA COLUMNA Y LA AGREGO AL DATAFRAME

data['Total Mins'] = data['Day Mins']+data['Eve Mins']+data['Night Mins']

print(data['Total Mins'])

print(data)
