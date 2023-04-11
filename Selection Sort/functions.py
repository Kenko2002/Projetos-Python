'''
|*| Ordenação de Listas em ordem alfabética |*|
    Recebe uma lista de tuplas a ser ordenada => Retorna a mesma lista ordenada
'''

def sSortAlpha(listToOrder):
    lista = listToOrder
    dictAbc = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
        "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, 
        "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, 
        "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, 
        "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, 
        "Z": 26,"2":0
    }

    #Ordenando por ordem alfabética
    for j in range(len(lista)-1):
        min_index = j
        for i in range (j, len(lista)):
            if dictAbc[lista[i][1][0]] < dictAbc[lista[min_index][1][0]]:
                min_index = i
        if dictAbc[lista[j][1][0]] > dictAbc[lista[min_index][1][0]]:
            lista[j], lista[min_index] = lista[min_index], lista[j]    
    
    return lista

'''
|*| Ordenação de Listas em ordem crescente |*|
    Recebe uma lista de tuplas a ser ordenada => Retorna a mesma lista ordenada
'''

def sSortKM(listToOrder):
    lista = listToOrder
    #Ordenando por ordem de KM
    for l in range(len(lista)-1):
        min_index = l
        for i in range (l, len(lista)):
            if int(lista[i][3]) < int(lista[min_index][3]):
                min_index = i
        
        if int(lista[l][3]) > int(lista[min_index][3]):
            lista[l], lista[min_index] = lista[min_index], lista[l]
    
    
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