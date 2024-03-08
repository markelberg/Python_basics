
archivo = open("newfile.txt", 'w')
archivo.write("Añadiendo texto al archivo desde el editor\n")
archivo = open("newfile.txt", 'a')
archivo.write("Adjuntando nuevo texto")
archivo.close()