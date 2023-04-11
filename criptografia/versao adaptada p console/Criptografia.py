def codificar_ou_decodificar(string_decodificada):
    string_codificada=""
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-'," "]
    
    for i in range(len(string_decodificada)):   #percorre a string que entrou na função
        letra=string_decodificada[i]            #salva a letra que está sendo analisada no momento em letra
        if letra==letra.upper():                #detecta se a letra analisada é maiuscula ou minuscula, e salva isso em variáveis.
            maiusculo,minusculo=True,False
        else:
            maiusculo,minusculo=False,True
        for j in range(len(alfabeto)):          #procura o índice no alfabeto que tenha a letra igual 
            if alfabeto[j]==letra or alfabeto[j]==letra.lower():
                indice_alfabeto=j
        
        if indice_alfabeto+1 in [2,4,6,8,10,12,14,16,18,20,22,24,26]:       #neste ponto filtra-se por par ou impar, e aplica as regras do enunciado
            if maiusculo==True:
                string_codificada+=alfabeto[indice_alfabeto-1].upper()
            if minusculo==True:
                string_codificada+=alfabeto[indice_alfabeto-1]
            
        if indice_alfabeto+1 in [1,3,5,7,9,11,13,15,17,19,21,23,25]:
            if maiusculo==True:
                string_codificada+=alfabeto[indice_alfabeto+1].upper()
            if minusculo==True:
                string_codificada+=alfabeto[indice_alfabeto+1]
                
        if indice_alfabeto+1==27:                                         #atentar a exceção do 0 e do ultimo indice para não dar out of range na hora de substituir.
            if maiusculo==True:
                string_codificada+="z".upper()
            if minusculo==True:
                string_codificada+="z"

        if indice_alfabeto+1==28:
            string_codificada+=" "
            
            
            
    return string_codificada


#a mesma função que criptografa pode ser usada pra descriptografar, basta fornecer a mensagem criptografa nos argumentos.

    
mensagem=input("Entre com o texto a ser processado:")
mensagem_processada=codificar_ou_decodificar(mensagem)
print(mensagem_processada)
input("ENTER")



