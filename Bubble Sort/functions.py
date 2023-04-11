'''
|*| Ordenação de Listas em ordem alfabética |*|
    Recebe uma lista de tuplas a ser ordenada => Retorna a mesma lista ordenada
'''

def bSortAlpha(listInput):
    dictAbc = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
        "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
        "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
        "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, 
        "Z": 26,"2":0
    }
    
    lista = listInput
    listLen = len(lista)

    for j in range(listLen - 1):
        for i in range(listLen - 1):
            if dictAbc[lista[i][1][0]] > dictAbc[lista[i+1][1][0]]:
                lista[i], lista[i+1] = lista[i+1] , lista[i]
    
    return lista

'''
|*| Ordenação de Listas em ordem decrescente |*|
    Recebe uma lista de tuplas a ser ordenada => Retorna a mesma lista ordenada
'''

def bSortKM(listInput):
    lista = listInput
    listLen = len(lista)

    for j in range(listLen - 1):
        for i in range(listLen - 1):
            if int(lista[i][3]) < int(lista[i+1][3]):
                lista[i], lista[i+1] = lista[i+1] , lista[i]
    
    return lista



'''
|*| Lendo arquivo e retornando linhas |*| 
    Recebe caminho de um arquivo => Retorna uma lista com todas as linhas
'''
def readArchive(path):
    archive = open(path,'r')
    list = []
    
    for line in archive:
        list.append(line[0:-2])
    
    return list

'''
|*| Criando tuplas para cada item de uma lista |*| 
    Recebe uma lista, e o local onde sera repartido => Retorna uma lista com items como tuplas
'''

def turnItemTuple(list,sliceLocal):
    listChanged = []
    for i in list:
        splited = i.split(sliceLocal) 
        listChanged.append(tuple(splited))
    
    return listChanged