import re

unidades = ["", "uno", "dos" ,"tres" ,"cuatro" ,"cinco" ,
            "seis" ,"siete" ,"ocho" ,"nueve"]
number_list = ["0", "1", "2" ,"3" ,"4" ,"5" ,
            "6" ,"7" ,"8" ,"9"] 
especiales = ["once", "doce","trece","catorce", "quince",
              "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veintiuno"
                , "veintidos","veintitres","veinticuatro", "veinticinco",
              "veintiseis", "venitisiete", "veintiocho", "veintinueve"]
special_list = ["11", "12", "13" ,"14" ,"15" ,"16" ,
            "17" ,"18" ,"19", "21", "22", "23" ,"24" ,"25" ,"26" ,
            "27" ,"28" ,"29"]        
decenas = ["", "diez","veinte","treinta","cuarenta","cincuenta", "sesenta",
           "setenta", "ochenta", "noventa"]
decenas_list = ["10","20","30","40","50", "60",
           "70", "80", "90"]
centenas = ["","ciento", "doscientos" ,"trescientos" ,"cuatrocientos" ,"quinientos" ,
            "seiscientos" ,"setecientos" ,"ochocientos" ,"novecientos"]
miles = ["","mil", "dos mil" ,"tres mil" ,"cuatro mil" ,"cinco mil" ,
            "seis mil" ,"siete mil" ,"ocho mil" ,"nueve mil"]         

def unaCifra(number):
    if number == "0":
        return "cero"
    if len(number) == 1:
        for i in range(len(unidades)): #obtiene numeros del 0 al 9
            if number == number_list[i]:
                return unidades[i]

def dosCifras(number):
    if int(number[0]) == 0:
        return unidades[int(number[1])]
    if int(number[1]) == 0:
        return decenas[int(number[0])]
    if int(number) > 10 and int(number) <= 29: #obtiene los especiales (11 a 29)
        for i in range(len(especiales)):
            if number == special_list[i]:
                return especiales[i]            
    if int(number) > 29 and int(number) < 100:
        x = decenas[int(number[0])]
        u = unidades[int(number[1])]
        return (x + " y " + u)
                                            
def tresCifras(number):
    if number == "100":
        return "cien"
    else:    
        for i in range(len(unidades)):
            if number[0] == number_list[i]:  
                return (centenas[i] + " " + dosCifras(number[1:3]))

def cuatroCifras(number):
    for i in range(len(unidades)):
        if number[0] == number_list[i]: 
            return (miles[i] + " " + tresCifras(number[1:4]))

def cincoCifras(number):
    return dosCifras(number[0:2]) + " mil " + tresCifras(number[2:5])

def seisCifras(number):
    if number[0:3] != "000":
        return tresCifras(number[0:3]) + " mil " + tresCifras(number[3:6])
    if number[0:3] == "000":
        return tresCifras(number[0:3]) + tresCifras(number[3:6])    

def sieteCifras(number):
    if int(number[0]) == 1:
        return "un millon " + seisCifras(number[1:7])
    if int(number[0]) > 1:
        return (str(unaCifra(number[0])) + " millones ") + seisCifras(number[1:7])

def ochoCifras(number):
        return str(dosCifras(number[0:2]) + " millones " + seisCifras(number[2:8]))

def nueveCifras(number):
        return str(tresCifras(number[0:3]) + " millones " + seisCifras(number[3:9]))

def diezCifras(number):
    return "mil millones"

number= input("ingrese el numero: ")

if number[0:2] == "00" or number[0:1] =="0" and number != "0":
    print("no deben contabilizarse ceros al comienzo del numero para que la aplicación funcione")    
elif int(number) <0 or int(number) >1000000000:
    print("el numero se encuentra fuera de rango de la aplicación (0 a 1.000.000.000)")  
else:
    if len(number) == 1:
        resultado= unaCifra(number)
    if len(number) == 2:    
        resultado= dosCifras(number)
    if len(number) == 3:    
        resultado= tresCifras(number)
    if len(number) == 4:    
        resultado= cuatroCifras(number)
    if len(number) == 5:    
        resultado= cincoCifras(number)
    if len(number) == 6:    
        resultado= seisCifras(number)
    if len(number) == 7:    
        resultado= sieteCifras(number) 
    if len(number) == 8:
        resultado= ochoCifras(number)
    if len(number) == 9:
        resultado= nueveCifras(number)
    if len(number) == 10:
        resultado= diezCifras(number)
    resultadoFinal = re.sub(' +', ' ', resultado)
    if "millones uno mil" in resultadoFinal:
        resultadoFinal=resultadoFinal.replace("millones uno mil","millones mil")
    if "millon uno mil" in resultadoFinal:
        resultadoFinal=resultadoFinal.replace("millon uno mil","millon mil") 
    if "uno m" in resultadoFinal:
        resultadoFinal=resultadoFinal.replace("uno m","un m")
    print(resultadoFinal)






