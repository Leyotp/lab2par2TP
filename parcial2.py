import re
import time 
import os
#Creacion del menu de seleccion
fname = 'File.txt'
def menu():
    print("[1] Especificar nombre de archivo y procesar su contenido")
    print("[0] Salir")
menu()
opcion = int (input("Escoja su opcion: "))
#Creacion de la funcion que leera el archivo 
def archi():

    file_name = str(input("Introduzca el nombre del archivo:  "))
   
    try:
        with open (fname, "r") as texto:
             #se manda a llamar al archivo de texto para usarlo como variable
            texto.read()
    
    except FileNotFoundError:
        msg ="El archivo" + file_name + "no se puede encontrar"
            #mensaje que aparecera si no se logra encontrar el archivo
        print(msg)

    else:
        #Se comienza con las operaciones
        inicio = time.time()
        num_palabras = 0
        num_lineas = 0
        num_caracteres = 0
        num_espacios = 0

        with open(fname, 'r') as f: 
        
            for line in f: 
            
                line = line.strip(os.linesep)     
                listado = line.split() 
                num_lineas = num_lineas + 1
                num_palabras = num_palabras + len(listado)   
                num_caracteres = num_caracteres + sum(1 for c in line  
                                if c not in (os.linesep, ' '))      
                num_espacios = num_espacios + sum(1 for s in line  
                                    if s in (os.linesep, ' '))     
        print("Numero de palabras del archivo " , file_name , " son: " , num_palabras)     
        print("Numero de lineas del archivo ", file_name , " son: " , num_lineas)     
        print("Numero de caracteres en el archivo ", file_name , " son: " , num_caracteres) 
        print("Numero de caracteres con espacio ", file_name , " son: " , (num_espacios + num_caracteres)) 
   
        ##Ahora se lee los caracteres especiales 
        with open(fname, "r") as  file:
            lineas = file.read().splitlines()
            
            unicos = set()
            for lin in lineas:
                unicos |= set(lin.split())

        print(f"Las palabras unicas del archivo " , file_name , " son igual a " , {len(unicos)})
        print ('Duracion: {} segundos'.format(time.time() - inicio))
    anykey=input("Presiona cualquier tecla para regresar al menu.  ")
##Se vuelve a llamar al menu para poder hacer de nuevo el proceso
while opcion != 0:
    if opcion == 1:
        archi()
    else:
        print("Opcion invalida")
    print()
    menu()
    opcion = int (input("Escoja su opcion: "))

print("Gracias por usar el software")
