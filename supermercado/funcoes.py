import os

def cls():
  os.system('clear')

def carregarprecos():
  arquivo=open('precos.txt','r')
  listaprecos=arquivo.readlines()
  arquivo.close()
  return listaprecos

def adicionarpreco(preco):
  arquivo=open('precos.txt','a')
  arquivo.write(preco+"\n")
  arquivo.close()

def carregarprodutos():
  arquivo=open('produtos.txt','r')
  listaprodutos=arquivo.readlines()
  arquivo.close()
  return listaprodutos

def adicionarprodutos(produto):
  arquivo=open('produtos.txt','a')
  arquivo.write(produto+"\n")
  arquivo.close()

def mostraritens_precos(listaprodutos,listaprecos):
  print("==========================")
  for i in range (len(listaprodutos)):
    print(f"{i}-{listaprodutos[i][0:(len(listaprodutos[i])-1)]} R${listaprecos[i][0:(len(listaprecos[i])-1)]}")
  print("==========================")

def realizarcompra():
  resposta=""
  listaprodutos=carregarprodutos()
  listaprecos=carregarprecos()
  mostraritens_precos(listaprodutos,listaprecos)
  teclado=int(input("Digite o Número do Item que deseja adicionar ao carrinho."))
  preco=str(listaprecos[teclado][0:len(listaprecos[teclado])-1])
  nome=str(listaprodutos[teclado][0:len(listaprodutos[teclado])-1])
  adicionarcarrinho(preco)
  adicionarcarrinhonomes(nome)
  resposta=input("Deseja Adicionar mais produtos? Sim/Não")
  if resposta=="Sim" or resposta=="SIM" or resposta=="sim":
    cls()
    realizarcompra()

def carregarcarrinho():
  arquivo=open('carrinho.txt','r')
  listacarrinho=arquivo.readlines()
  arquivo.close()
  return listacarrinho

def adicionarcarrinho(produto):
  arquivo=open('carrinho.txt','a')
  arquivo.write(produto+"\n")
  arquivo.close()

def carregarcarrinhonomes():
  arquivo=open('carrinhonomes.txt','r')
  listacarrinhonomes=arquivo.readlines()
  arquivo.close()
  return listacarrinhonomes

def adicionarcarrinhonomes(produto):
  arquivo=open('carrinhonomes.txt','a')
  arquivo.write(produto+"\n")
  arquivo.close()

def somalista(lista):
  novalista=[]
  soma=0
  for i in lista:
    novalista.append(float(i))
  for i in novalista:
    soma+=i
  return soma

def mostrarcarrinho():
  listacarrinho=carregarcarrinho()
  listacarrinhonomes=carregarcarrinhonomes()
  print("==========================")
  for i in range(len(listacarrinho)):
    print(listacarrinhonomes[i][0:len(listacarrinhonomes[i])-1],listacarrinho[i][0:len(listacarrinho[i])-1])
  print("==========================")
  print("TOTAL:",somalista(listacarrinho))
  input("ENTER")

def zerar_carrinho():
  arquivo=open("carrinho.txt","w")
  arquivo.write("")
  arquivo.close()
  arquivo=open("carrinhonomes.txt","w")
  arquivo.write("")
  arquivo.close()

def registraritem():
  arquivo=open('produtos.txt','a')
  arquivo.write(input("Digite o Nome do Produto")+"\n")
  arquivo.close()
  arquivo=open('precos.txt',"a")
  arquivo.write(input("Digite o Preço do Produto")+"\n")
  arquivo.close()

def removeritem():
  listaprodutos=carregarprodutos()
  listaprecos=carregarprecos()
  mostraritens_precos(listaprodutos,listaprecos)
  teclado=int(input("Digite o Número do Item que você deseja remover do Banco de Dados."))
  listaprodutos.pop(teclado)
  listaprecos.pop(teclado)
  salvarprodutos(listaprodutos)
  salvarprecos(listaprecos)

def salvarprodutos(lista):
  arquivo=open('produtos.txt','w')
  arquivo.write("")
  arquivo.close()
  arquivo=open('produtos.txt','a')
  for i in lista:
    arquivo.write(i)
  arquivo.close()

def salvarprecos(lista):
  arquivo=open('precos.txt','w')
  arquivo.write("")
  arquivo.close()
  arquivo=open('precos.txt','a')
  for i in lista:
    arquivo.write(i)
  arquivo.close()
