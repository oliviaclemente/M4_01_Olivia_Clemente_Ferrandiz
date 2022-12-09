import pandas as pd
d1=pd.read_csv("imdb_titulos.csv")
d1
d2=pd.read_csv("imdb_elenco.csv")
d2
print(d1.head(5)) # muestra los primeros 5 registros
print(d2.head(5)) # muestra los primeros 5 registros
print(d1.tail(5)) # muestra los ultimos 5 registros
print(d2.tail(5)) # muestra los ultimos 5 registros

print(d1["Dracula"].value_counts()) # cuenta los registros de la columna Dracula
print(d2["Dracula"].value_counts()) # cuenta los registros de la columna Dracula

print(len(d1)) # cuenta los registros de la tabla d1
print(len(d2)) # cuenta los registros de la tabla d2

print(d1.sort_values(by='year').head()) # ordena los registros de la tabla d1 por año
print(d2.sort_values(by='year').head()) # ordena los registros de la tabla d2 por año

print(d1[d1['title'].str.contains('Dracula')]) # muestra los registros que contienen la palabra Dracula
print(d2[d2['title'].str.contains('Dracula')]) # muestra los registros que contienen la palabra Dracula

print(d1['title'].value_counts().head(10))  # muestra los 10 registros mas repetidos de la columna title
print(d2['title'].value_counts().head(10))  # muestra los 10 registros mas repetidos de la columna title

print(d1[d1['year'] == 1950]) # muestra los registros del año 1950
print(d2[d2['year'] == 1950]) # muestra los registros del año 1950

print(d1[d1['year'] == 1950].sort_values(by='title')) # muestra los registros del año 1950 ordenados por titulo
print(d2[d2['year'] == 1950].sort_values(by='title')) # muestra los registros del año 1950 ordenados por titulo

print(d1[d1['year'] >= 1950 & (d1['year'] <= 1959)].sort_values(by='title')) # muestra los registros del año 1950 al 1959 ordenados por titulo
print(d2[d2['year'] >= 1950 & (d2['year'] <= 1959)].sort_values(by='title')) # muestra los registros del año 1950 al 1959 ordenados por titulo

print(d2[d2['title'] == 'The Godfather'].sort_values(by='n')) # muestra los registros del titulo The Godfather ordenados por n
print(len(d2[d2['title'] == 'The Godfather'].sort_values(by='n'))) # cuenta los registros del titulo The Godfather ordenados por n

print(d2[d2['title'] == 'Dracula' & (d2['year'] == 1958)].sort_values(by='year')) # muestra los registros del titulo Dracula del año 1958 ordenados por año

print(len(d2[d2['character'] == 'Bruce Wayne'])) # cuenta los registros del personaje Bruce Wayne

print(len(d2[(d2['type'] == 'actor') & (d2['year'] <= 1959)])) # cuenta los registros de actores del año 1959 o anterior
print(len(d2[(d2['type'] == 'actress') & (d2['year'] <= 1959)])) # cuenta los registros de actores del año 1959 o anterior
