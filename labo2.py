import re
import time 

inicio = time.time()


#Creacion del menu de seleccion
def menu():
    print("[1] Especificar nombre de archivo y procesar su contenido")
    print("[0] Salir")
menu()
opcion = int (input("Escoja su opcion: "))
#Creacion de la funcion que leera el archivo 
def archi():

    file_name = str(input("Introduzca el nombre del archivo:  "))
   
    try:
        with open ("file.txt", "r") as texto:
             #se manda a llamar al archivo de texto para usarlo como variable
            texto_data = texto.read()
    
    except FileNotFoundError:
        msg ="El archivo" + file_name + "no se puede encontrar"
            #mensaje que aparecera si no se logra encontrar el archivo
        print(msg)

    else:
        #Se comienza con las operaciones
        contenido = texto_data.split()
        numero_palabras = len(contenido)

        #Se cuenta la cantidad de palabras
        print("El archivo " + file_name + " contiene una cantidad de " + str(numero_palabras) + " palabras." )

        #se vuelve a abrir el archivo ya que se ocupo y se cerro en la operacion pasada.
        texto1 = open ("file.txt", 'r')
        

        print("El archivo  " + file_name + " "  + str(len(texto1.readlines())) + " lineas ")
        texto1.close()

        count = 0
        for lin in contenido:
            charac_count=re.findall("(\S)", lin.strip())
            if charac_count:
                count += len(charac_count)
        charac_quant = len(charac_count)
        #Esto es lo que cuenta el numero de caracteres en el archivo
        print("El archivo posee " ,  charac_quant , " caracteres con espacio")
        print("El archivo tiene " , count , " caracteres sin espacio")

        ##Ahora se lee los caracteres especiales 
        with open("file.txt", "r") as  file:
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
