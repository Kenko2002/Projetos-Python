def carregar_database():
    import pickle
    with open('database.bin','rb') as f:
        a=pickle.load(f) #Nomes (lista strings)
        b=pickle.load(f) #CPFs (lista strings)
        c=pickle.load(f) #Crédito Social (lista inteiros)
        d=pickle.load(f) #Senhas (lista strings)
    return a,b,c,d

def salvar_database(a,b,c,d):
    import pickle
    with open("database.bin","wb") as f:
        pickle.dump(a,f)
        pickle.dump(b,f)
        pickle.dump(c,f)
        pickle.dump(d,f)



def cadastrar_cidadao(a,b,c,d):
    nome=input("Digite o Nome do Cidadão: ")
    CPF=input("Digite o CPF (inclua pontos e traços): ")
    credito=100
    senha=input("Defina a sua Senha: ")
    if (not nome in a)and(not CPF in b):
        print("Parabéns, você ganhou 100 créditos por se registrar!")
        a.append(nome)
        b.append(CPF)
        c.append(100)
        d.append(senha)
        salvar_database(a,b,c,d)
        input("ENTER")
    else:
        print("Erro no registro, esse nome ou CPF já foi registrado no sistema.")

def remover_cidadao(a,b,c,d):
    CPF=input("Digite o CPF que será cancelado pelo Estado (Inclua traços, pontos, etc.): ")
    ID=0
    for i in range(len(b)):
        if b[i]==CPF:
            ID=i
            break

    print("Nome:",a[ID])
    print("CPF:",b[ID])
    print("Crédito:",c[ID])
    tec=input("Esse é o Cidadão que deve ser Removido? s/n")
    tec=tec.upper()
    while tec!="S" and tec!="N":
        tec=input("Esse é o Cidadão que deve ser Removido? s/n")
        tec=tec.upper()
    if tec=="S":
        a.pop(ID)
        b.pop(ID)
        c.pop(ID)
        d.pop(ID)
        salvar_database(a,b,c,d)

def listar_scores(a,b,c,d):
    print("===================================================")
    a,c=ordenar_scores(a,c)
    for i in range(len(a)):
        print("Ranking:",i+1," \t Nome:",a[i]," \t CPF:",b[i]," \t Crédito:",c[i]," \t Senha:",d[i])
    print("===================================================")
    
def ordenar_scores(a,c):
    for i in range (len(c)):
        for j in range (len(c)):
            if c[i]>c[j]:
                aux=c[i]
                c[i]=c[j]
                c[j]=aux

                aux=a[i]
                a[i]=a[j]
                a[j]=aux
    return a,c

def gerenciar_credito(a,b,c,d):
    CPF=input("Digite o CPF do moderador (inclua pontos e traços): ")
    senha=input("digite a Senha do moderador: ")
    if CPF == "176.846.367-07" and senha=="Macaco123":
        print("Bem vindo, Líder supremo, por favor, recompensa teus servos e pune teus inimigos.")
        tec=input("1-Recompensar  2-Punir")
        while tec!="1" and tec!="2":
            tec=input("1-Recompensar  2-Punir")
        recompensa=0
        punicao=0
        if tec=="1":
            CPF=input("Insira o CPF a ser Recompensado: ")
            recompensa=int(input("Quantos créditos sociais essa pessoa ganhará?"))
        if tec=="2":
            CPF=input("Insira o CPF a ser Punido: ")
            punicao=int(input("Quantos créditos sociais essa pessoa perderá?"))

        ID=0
        for i in range(len(b)):
            if b[i]==CPF:
                ID=i
                break
        
        c[ID]=c[ID]+recompensa-punicao
        salvar_database(a,b,c,d)
        print("Processo concluído com Sucesso.")

def main():
    import pickle
    quebrar=False
    while True:
        a,b,c,d=carregar_database()
        print("Bem Vindo Ao Sistema de Crédito Social do Ranho!")
        print("A seguir segue as funcionalidades do sistema:")
        print("1- Adicionar novo Cidadão ao Sistema")
        print("2- Remover Cidadão do Sistema")
        print("3- Conferir Lista de Cidadões cadastrados")
        print("4- Adicionar/Remover Crédito Social a conta de um Cidadão")
        print("5- Fechar")


        teclado=input("Selecione a Função:")
        while teclado!="1" and teclado!="2" and teclado!="3" and teclado!="4" and teclado!="5" and teclado!="6":
            teclado=input("Selecione a Função:")
        
        if teclado=="1":
            cadastrar_cidadao(a,b,c,d)
        if teclado=="2":
            remover_cidadao(a,b,c,d)
        if teclado=="3":
            listar_scores(a,b,c,d)
        if teclado=="4":
            gerenciar_credito(a,b,c,d)
        if teclado=="5":
            quebrar=True

        if quebrar==True:
            break
main()
