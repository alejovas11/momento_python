diccionario = {}
texto = input("Digite una oración:").lower()

oracion = texto.split(" ")


for x in oracion:
	if x in dict:
		dict[x]+=1 
	else:
		dict[x]=1	

for palabra, repeticion in dict.items():
	print (palabra," = ",repeticion)