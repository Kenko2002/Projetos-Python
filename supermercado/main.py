from funcoes import *

def main():
  while True:
    cls()
    teclado=input("1-Adicionar Ao Carrinho \n2-Registrar Novo Item no banco de dados \n3-Remover Item do banco de dados \n4-Mostrar Itens e Preços do banco de dados\n5-Mostrar Carrinho\n6-Zerar Carrinho")
    while teclado!='1' and teclado!='2' and teclado!='3' and teclado!='4' and teclado!='5' and teclado!='6':
      input("1-Adicionar Ao Carrinho \n2-Registrar Novo Item \n3-Remover Item \n4-Mostrar Itens e Preços\n5-Mostrar Carrinho\n6-Zerar Carrinho")
      cls()
    cls()
    if teclado=='1':
      realizarcompra()
    if teclado=='2':
      registraritem()
    if teclado=='3':
      removeritem()
    if teclado=='4':
      listaprodutos=carregarprodutos()
      listaprecos=carregarprecos()
      mostraritens_precos(listaprodutos,listaprecos)
      input("ENTER")
    if teclado=='5':
      mostrarcarrinho()
    if teclado=='6':
      zerar_carrinho()


main()
