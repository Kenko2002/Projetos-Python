'''
Questão 13. Desenvolva uma função na linguagem Python que recebe por parâmetro um
texto, calcula e retorna um valor representando a sua pontuação com base nas seguintes
regras:

• A pontuação de uma palavra é 2 se a palavra contém um número ímpar de vogais,
caso contrário, o escore da palavra é igual a 1. Letras maiúsculas e minúsculas
devem ser consideradas iguais. Considere que o texto de entrada não possui
nenhum símbolo de acentuação. A lista de vogais é: [‘a’, ‘e’, ‘i’, ‘o’, ‘u’]
• A pontuação total do texto é dada pela média das pontuações das suas palavras,
ou seja, soma as pontuações das palavras individualmente e divide pelo total de
palavras do texto.
• Fragmente o texto por espaço em branco para identificar as suas palavras.

Exemplos:
a) Entrada: Python e muito fácil
Saída: 1.75
b) Entrada: Ola Mundo
Saída: 1.00
'''

def pontos(texto):
    pontuacao_texto=float(0)
    lista_pontuacoes_palavras=[]
    palavras=texto.split(" ")
    for i in range(len(palavras)):
        vogais=0
        pontuacao_palavra=0
        for j in range(len(texto)):                     #criterio 1, numero de vogais
            if texto[j].lower() in ['a', 'e', 'i', 'o', 'u']:
                vogais+=1
        if vogais%2!=0:                                 #confere se o número é impar, em caso verdadeiro, entra na condicional.
            pontuacao_palavra=2
        else:
            pontuacao_palavra=1
        lista_pontuacoes_palavras.append(pontuacao_palavra)
        
    for i in range (len(lista_pontuacoes_palavras)):    #soma a pontuacao de cada palavra no texto
        pontuacao_texto+=lista_pontuacoes_palavras[i]
    pontuacao_texto=pontuacao_texto/len(lista_pontuacoes_palavras) #depois tira a média

    return pontuacao_texto


print(pontos("Ola Mundo"))
            
