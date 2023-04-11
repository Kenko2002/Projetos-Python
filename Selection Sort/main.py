from functions import *
def main():
    #Variavéis
    listToOrder = []
    alphabeticList = []
    kmList = []
    archivePath = "bdveiculos.txt"

    #Processamento
    listToOrder = readArchive(archivePath)
    listToOrder = turnItemTuple(listToOrder,",")

    alphabeticList = sSortAlpha(listToOrder)
    

    #Ordem alfabética por modelo
    for pos, item in enumerate(alphabeticList):
        a = open("bdveiculosselecao.txt", "a")
        if pos == 0:
            a.write("Ordem alfabetica por modelo:\n\n")

        modelo = item[1]
        marca = item[2]
        
        
        a.write(f"{pos:04} --- {modelo} --- {int(item[3]):06} --- {marca} --- {item[0]}\n")
        a.close()
    
    kmList = sSortKM(listToOrder)

    #Ordem crescente por km
    for pos, item in enumerate(kmList):
        a = open("bdveiculosselecao.txt", "a")
        if pos == 0:
            a.write("\n\n\nOrdem decrescente por KM:\n\n")
        modelo = item[1]
        marca = item[2]
        
        a.write(f"{pos:04} --- {modelo} --- {int(item[3]):06} --- {marca} --- {item[0]}\n")
        a.close()

if __name__ == "__main__":
    main()
