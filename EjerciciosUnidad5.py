import re

def pedirNumeroEntero():

    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("OPCION:"))
            correcto = True
        except ValueError:
            print("-----------------------------------------------------------------------------------------" + "\n" +
                   'Opcion no validad' + "\n" + "VUELVA A INTENTAR"+ "\n" + 
                   "-----------------------------------------------------------------------------------------")


    return num


salir = False
opcion = 0

while not salir:
    print("-----------------------------------------------------------------------------------------")
    print("Elija una opcion")
    print ("1. Sentencia de asignación." +"\n"+ 
           "2. Operaciones aritméticas básicas." + "\n" +
           "3. Expresiones booleanas básicas." + "\n" + 
           "4. Formulas más complejas del tipo c ."  + "\n"+
           "5. Estructura de control." + "\n" + 
           "6. salir")
    print("-----------------------------------------------------------------------------------------")
   

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Sentencia de asignación. ")
        f = open ("EjemploSentencia.txt").read() 
        ExpReg = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'  
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)

    elif opcion == 2:
        print ("Operaciones aritméticas básicas")
        f = open("EjemploOperacionesAritméticas.txt").read()
        ExpReg = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)
           
    elif opcion == 3:
        print ("Expresiones booleanas básicas")
        f = open("EjemploExpresionesBooleanas.txt").read()
        ExpReg = r'([A-Za-z0-9]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)

    elif opcion == 4:
        print("Formulas más complejas del tipo c = a op ( b op d)")    
        f = open("EjemploFormulasComplejas.txt").read()
        ExpReg = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)

    elif opcion == 5:
        print("El encabezado de estructura de control. if, while, for, etc")
        f = open("EjemploEstructuraControl.txt").read()
        ExpRegIf = r'(if+\s*[A-Za-z0-9-]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-]+\s*:)'
        ExpRegWhile = r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
        ExpRegFor = r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)' 
        expIf = re.findall(ExpRegIf, f, flags=re.MULTILINE)
        expWhile = re.findall(ExpRegWhile , f, flags=re.MULTILINE)
        expFor = re.findall(ExpRegFor, f, flags=re.MULTILINE)
        print (expIf)
        print("")
        print (expWhile)
        print("")
        print (expFor)

    elif opcion == 6:
            salir = True
    else:
        print ("VUELVA A INTENTAR" + "\n" + "Elija una obcion entre 1 al 6")

