# Reto #28: Expresión matemática
#### Dificultad: Media | Publicación: 10/07/23 | Corrección: 17/07/23
## Enunciado
#
# Crea una función que reciba una expresión matemática (String)
# y compruebe si es correcta. Retornará true o false.
# - Para que una expresión matemática sea correcta debe poseer
#   un número, una operación y otro número separados por espacios.
#   Tantos números y operaciones como queramos.
# - Números positivos, negativos, enteros o decimales.
# - Operaciones soportadas: + - # / % 
#
# Ejemplos:
# "5 + 6 / 7 - 4" -> true
# "5 a 6" -> false

import re

def expreMate(expre:str):
    regen= r"^[-+]?\d*(\.\d{1,2})?[\s\S][\+\-\*\/\%][\s\S][-+]?\d*(\.\d{1,2})?([\s\S][\+\-\*\/\%][\s\S][-+]?\d*(\.\d{1,2})?[\s\S][\+\-\*\/\%][\s\S][-+]?\d*(\.\d{1,2})?)?$"
    #regen1=r'^\d?[\s\S][\+\-\*\/\%][\s\S]\d?$'

    encExpMat = re.match(regen,expre)
    
    #encntExpMat = re.fullmatch(regen,expre)
    #encntExpMat1 = re.fullmatch(regen1,expre)
    #encntExpMat2 = re.search(regen,expre)
    #encntExpMat3 = re.search(regen1,expre)
 
    print ("encntExpMat=",encntExpMat)
    #print ("encntExpMat1",encntExpMat1)
    #print ("encntExpMat2",encntExpMat2)
    #print ("encntExpMat3",encntExpMat3)

    #if encExpMat != None or encntExpMat2 !=None:
        #return True
    #else:
        #return False
    if encExpMat != None:
        return True
    else:
        return False

if __name__ == "__main__":
    print(expreMate("-4 + 5.80"))
    print(expreMate("5 + 6 / 7 - 4"))
    print(expreMate("4 a 6"))
    print(expreMate("4.49 + 5.90"))
    print(expreMate("4+5"))
