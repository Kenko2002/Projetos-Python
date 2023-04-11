'''
Questão 14. Escreva um programa em Python para armazenar uma agenda de telefones
em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é
o nome da pessoa. Seu programa deve ter as seguintes funções:

• incluir_novo_nome – essa função acrescenta um novo nome na agenda, com um
ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
• incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa
deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir
o novo nome.
• excluir_telefone – essa função exclui um telefone de uma pessoa que já está na
agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
• excluir_nome – essa função exclui uma pessoa da agenda.
• consultar_telefone – essa função retorna os telefones de uma pessoa na agenda.

Seu programa deve ter dois arquivos de código, um arquivo somente com as
implementações das funções e um outro arquivo contendo um menu com uma opção para
que o usuário execute cada uma das funções listadas anteriormente.

Seu programa deve
ficar repetindo a exibição do menu e respondendo as ações do usuário até que ele digite
a opção 6 – Sair.
'''



def menu(dicionario):
    teclado=""
    while teclado!="6":
        print("Bem vindo a sua agenda virtual, O que gostaria de fazer?")
        print("1- Incluir Novo Nome")
        print("2- Incluir Telefone")
        print("3- Excluir Telefone")
        print("4- Excluir Nome")
        print("5- Consultar Telefone")
        print("6- Sair")
        teclado=input()
        if teclado=="1":
            nome=input("Digite o Nome do Novo Contato")
            teclado2=""
            lista_numeros=[]
            while teclado2!="0":
                teclado2=input("Digite o Número, ou digite 0 para parar de inserir novos números para esse contato.")
                if teclado2!="0":
                    lista_numeros.append(teclado2)
            dicionario=incluir_novo_nome(nome,lista_numeros,dicionario)
        if teclado=="2":
            incluir_telefone(dicionario)
        if teclado=="3":
            excluir_telefone(dicionario)
        if teclado=="4":
            excluir_nome(dicionario)
        if teclado=="5":
            consultar_telefone(dicionario)
        if teclado=="6":
            sair()

def incluir_novo_nome(nome,lista_numeros,dicionario):
    contato={nome:lista_numeros}
    dicionario.update(contato)
    return dicionario

def incluir_telefone(dicionario):
    nome=input("Digite o nome do contato ao qual deseja adicionar um telefone")
    telefone=input("Digite o Telefone a ser adicionado.")
    if nome in dicionario:
        dicionario[nome].append(telefone)
    else:
        print("Esse nome não existe na sua lista, deseja adicionar-lo?")
        teclado=input("Sim / Não")
        if teclado=="Sim":
            lista_numeros=[]
            lista_numeros.append(telefone)
            incluir_novo_nome(nome,lista_numeros,dicionario)
    return dicionario
    
def excluir_telefone(dicionario):                                           #nessa função o enunciado n deixou claro se era pra pedir o telefone 
    nome=input("Digite o nome do contato cujo qual você deseja deletar um telefone") #ou se era só pra remover um número qualquer dentre os números que o contato tenha.
    telefone=input("Digite o Telefone que precisa ser removido")                #entao eu fiz como eu imagino q esteja certo, pedir o numero e remover esse numero
    if len(dicionario[nome])==1:
        dicionario.pop(nome)
    else:       
        for i in range(len(dicionario[nome])):
            if dicionario[nome][i]==telefone:
                dicionario[nome].pop(i)
    return dicionario

def excluir_nome(dicionario):
    teclado=input("Digite o nome do contato que você deseja excluir")
    dicionario.pop(teclado)
    return dicionario

def consultar_telefone(dicionario):
    teclado=input("Digite o nome da pessoa que você deseja consultar os telefones")
    if teclado in dicionario:
        print(dicionario[teclado])
    else:
        print("o nome não consta na agenda")
        
def sair():
    print("Até a próxima vez, usuário!")
    input("ENTER para sair do programa")

def main():
    dicionario={}
    menu(dicionario)
main()
    
