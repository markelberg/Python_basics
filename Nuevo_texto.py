
archivo = open("newfile.txt", 'w')
archivo.write("Añadiendo texto al archivo desde el editor\n")
archivo = open("newfile.txt", 'a')
archivo.write("Adjuntando nuevo texto")
archivo.close()

#Es más óptimo y "limpio" si lo hacemos con with ('r' para read, 'w' para write, 'a' para append)

with open("newfile.txt", 'w') as archivo:
    lectura = archivo.write("Sobreescribiendo el txt con with")
    print(lectura)

