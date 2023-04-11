from functions import *
def main():
    #Variavéis
    listToOrder = []
    archivePath = "bdveiculos.txt"
    alphabeticList = []
    kmList = []

    #Processamento
    listToOrder = readArchive(archivePath)
    listToOrder = turnItemTuple(listToOrder,",")

    alphabeticList = bSortAlpha(listToOrder)
    print(alphabeticList)

    #Alfabética pelo modelo
    for pos, item in enumerate(alphabeticList):
        a = open("bdveiculosbolha.txt", "a")
        if pos == 0:
            a.write("Ordem alfabetica por modelo:\n\n")

        modelo = item[1]
        marca = item[2]
        
        
        a.write(f"{pos:04} --- {modelo} --- {int(item[3]):06} --- {marca} --- {item[0]}\n")
        a.close()
    
    kmList = bSortKM(listToOrder)

    for pos, item in enumerate(kmList):
        a = open("bdveiculosbolha.txt", "a")
        if pos == 0:
            a.write("\n\n\nOrdem decrescente por KM:\n\n")

        modelo = item[1]
        marca = item[2]
        
        
        a.write(f"{pos:04} --- {modelo} --- {int(item[3]):06} --- {marca} --- {item[0]}\n")
        a.close()

if __name__ == "__main__":
    main()
