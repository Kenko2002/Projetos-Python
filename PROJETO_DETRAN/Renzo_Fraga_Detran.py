import pickle
import os

def cls():
  os.system('clear')

def carregar_tudo():
  with open("multas.bin","rb") as f:
    a=pickle.load(f) #dict motoristas
    b=pickle.load(f) #dict veiculos
    c=pickle.load(f) #dict infracoes
    d=pickle.load(f) #dict gravidade
    return a,b,c,d

def salvar_tudo(a,b,c,d):
  with open("multas.bin","wb") as f:
    pickle.dump(a,f)
    pickle.dump(b,f)
    pickle.dump(c,f)
    pickle.dump(d,f)

def mostrar_menu():
  print("1- Cadastrar um novo motorista")
  print("2- Cadastrar um novo veículo.")
  print("3- Alterar proprietário de um veículo.")
  print("4- Cadastrar uma nova infração")
  print("5- Sair do sistema.")
  print("6- Mostrar Dados Salvos")
  print("7- Remover Motorista do Sistema")
  print("8- Remover Veículo do Sistema")
  print("9- Remover Infração do Sistema")
  teclado=input("")
  while teclado!="1" and teclado!="2" and teclado!="3" and teclado!="4" and teclado!="5" and teclado!="6" and teclado!="7" and teclado!="8" and teclado!="9":
    teclado=input("")
  return teclado

def cadastrar_motorista(dict_motoristas):
  #"01234567" : ("Seu Madruga", (15 ,10 ,2019)) 
  CNH=input("Insira a CNH do motorista: ")
  nome=input("Insira o Nome do Motorista: ")
  vencimento_CNH=input("Insira a data de Vencimento da CNH: ")
  vencimento_CNH=converter_string_para_tupla(vencimento_CNH)
  if CNH in dict_motoristas:
    print("Esse CNH já foi registrado no Sistema.")
  else:
    dict_motoristas.update({CNH:(nome,vencimento_CNH)})

def converter_string_para_tupla(string):
  #entrada: 22/10/2002  saida:(22,10,2002)
  dia=string[0:2]
  mes=string[3:5]
  ano=string[6:]
  return (dia,mes,ano)

def cadastrar_veiculo(dict_veiculos):
  placa=input("Insira a Placa do Veículo:")
  CNH=input("Insira a CNH do proprietário")
  modelo=input("Insira o Modelo do veículo")
  cor=input("Insira a Cor do veículo")
  if placa in dict_veiculos:
    print("Essa Placa já foi registrada no Sistema.")
  else:
    dict_veiculos.update({placa:(CNH,modelo,cor)})
  
def alterar_proprietario_de_veiculo(dict_veiculos,dict_motoristas):
  placa=input("Insira a Placa do Veículo")
  CNH=input("Insira a CNH do novo proprietário")
  if not placa in dict_veiculos:
    print("Essa Placa Não Foi Registrada no Sistema.")
  elif not CNH in dict_motoristas:
    print("Essa CNH não foi registrada no Sistema.")
  else:
    dict_veiculos[placa]=(CNH,dict_veiculos[placa][1],dict_veiculos[placa][2])

def adicionar_infracao(dict_infracoes,dict_veiculos):
  ID=gerar_identificador_infracao(dict_infracoes)
  data=input("Insira a Data da Infração: ")
  data=converter_string_para_tupla(data)
  placa=input("insira a Placa do Veículo envolvido: ")
  natureza_da_inflacao=input("1-Leve 2-Média 3-Grave 4-Gravíssima")
  while natureza_da_inflacao!="1" and natureza_da_inflacao!="2" and natureza_da_inflacao!="3" and natureza_da_inflacao!="4":
    natureza_da_inflacao=input("1-Leve 2-Média 3-Grave 4-Gravíssima")
  if natureza_da_inflacao=="1":
    natureza_da_inflacao="Leve"
  if natureza_da_inflacao=="2":
    natureza_da_inflacao="Media"
  if natureza_da_inflacao=="3":
    natureza_da_inflacao="Grave"
  if natureza_da_inflacao=="4":
    natureza_da_inflacao="Gravissima"
  if placa in dict_veiculos:
    dict_infracoes.append((ID,data,placa,natureza_da_inflacao))
  else:
    print("A Placa em questão não consta nos registros.")
    input("ENTER")

def gerar_identificador_infracao(dict_infracoes):
  id_gerado=len(dict_infracoes)+1
  return id_gerado

def converter_tupla_para_string(tupla):
  acumulador=""
  for i in tupla:
    i=str(i)
    acumulador=acumulador+i+"/"
  acumulador=acumulador[0:(len(acumulador)-1)]
  return acumulador

def mostrar_dados(dict_motoristas,dict_veiculos,dict_infracoes):
  #dict_motoristas
  cls()
  print("MOTORISTAS")
  print("==========================")
  for i in dict_motoristas:
    print(f"CNH: {i}\nMotorista: {dict_motoristas[i][0]}\nData De Vencimento da CNH: {converter_tupla_para_string(dict_motoristas[i][1])}")
    print("==========================")
  input("ENTER")
  #dict_veiculos
  cls()
  print("VEÍCULOS")
  print("==========================")
  for i in dict_veiculos:
    print(f"Placa:{i} \nCNH do dono:{dict_veiculos[i][0]} \nModelo:{dict_veiculos[i][1]} \nCor:{dict_veiculos[i][2]}")
    print("==========================")
  input("ENTER")
  #dict_infracoes
  cls()
  print("INFRAÇÕES")
  print("==========================")
  for i in dict_infracoes:
    id=i[0]
    data=i[1]
    placa=i[2]
    gravidade=i[3]
    print(f"ID:{id} \nData da Infração:{converter_tupla_para_string(data)} \nPlaca:{placa} \nGravidade Da Infração:{gravidade}")
    print("==========================")
  input("ENTER")

def remover_motorista(dict_motoristas):
  CNH_a_ser_removida=input("Digite o Número da CNH que será removida do sistema")
  if CNH_a_ser_removida in dict_motoristas:
    dict_motoristas.pop(CNH_a_ser_removida)
  else:
    print("A CNH não consta nos registros")
    input("ENTER")

def remover_veiculo(dict_veiculos):
  placa_a_ser_removida=input("Digite a placa do veículo que será removido do sistema")
  if placa_a_ser_removida in dict_veiculos:
    dict_veiculos.pop(placa_a_ser_removida)
  else:
    print("A placa não consta nos registros.")
    input("ENTER")

def remover_infracoes(dict_infracoes):
  id_a_ser_removido=input("Digite o ID da infração que será removida do sistema")
  if id_a_ser_removido in dict_infracoes:
    dict_infracoes.pop(id_a_ser_removido)
  else:
    print("O ID não consta no Sistema.")
  
def main():
  dict_motoristas,dict_veiculos,dict_infracoes,dict_gravidade=carregar_tudo()

  while True:
    salvar_tudo(dict_motoristas,dict_veiculos,dict_infracoes,dict_gravidade)
    cls()
    teclado=mostrar_menu()
    if teclado=="1":
      cadastrar_motorista(dict_motoristas)
    if teclado=="2":
      cadastrar_veiculo(dict_veiculos)
    if teclado=="3":
      alterar_proprietario_de_veiculo(dict_veiculos,dict_motoristas)
    if teclado=="4":
      adicionar_infracao(dict_infracoes,dict_veiculos)
    if teclado=="5":
      salvar_tudo(dict_motoristas,dict_veiculos,dict_infracoes,dict_gravidade)
      break
    if teclado=="6":
      mostrar_dados(dict_motoristas,dict_veiculos,dict_infracoes)
    if teclado=="7":
      remover_motorista(dict_motoristas)
    if teclado=="8":
      remover_veiculo(dict_veiculos)
    if teclado=="9":
      remover_infracoes(dict_infracoes)
main()
