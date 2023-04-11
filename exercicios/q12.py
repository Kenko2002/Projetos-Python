'''Questão 12. Implemente uma função em Python chamada sublista que receba duas listas
por parâmetro lista_1 e lista_2 e retorna True se a lista_1 é uma sublista da lista_2, ou
False caso contrário. Uma lista 1 é considerada uma sublista de uma lista 2, se todos os
elementos da lista 1 aparecem na lista 2 na mesma ordem em que eles ocorrem na lista 1.
Crie uma função principal e teste sua função com alguns exemplos.
Exemplos:
• [15, 1, 100] é uma sublista de [20, 15, 30, 50, 1, 100]
• [15, 50, 20] não é uma sublista de [20, 15, 30, 50, 1, 100]'''


def detectar_sublista(sublista,lista):
    cont=0
    for i in range (len(sublista)):
        for j in range(len(lista)):
            if sublista[i]==lista[j]:
                cont+=1
    if cont==len(sublista):
        return True
    else:
        return False


sublista=[15,1,100]
lista=[20,15,30,50,1,100]


eh_sublista=detectar_sublista(sublista,lista)

if eh_sublista==True:
    print(sublista,"é uma sublista de",lista)
else:
    print(sublista,"não é uma sublista de",lista)
