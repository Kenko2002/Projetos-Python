'''QUESTAO 15'''
def conferir_cnpj(cnpj):
    #inicio etapa 1
    cnpj_digito_verificador_1=int(cnpj[0])*5+int(cnpj[1])*4+int(cnpj[2])*3+int(cnpj[3])*2+int(cnpj[4])*9+int(cnpj[5])*8+int(cnpj[6])*7+int(cnpj[7])*6+int(cnpj[8])*5+int(cnpj[9])*4+int(cnpj[10])*3+int(cnpj[11])*2 #etapa a
    resto=cnpj_digito_verificador_1%11 #etapa b
    if resto < 2:                       #etapa c
        cnpj_digito_verificador_1=0
    else:
        cnpj_digito_verificador_1=11-resto

    #inicio etapa 2
    cnpj_digito_verificador_2=int(cnpj[0])*6+int(cnpj[1])*5+int(cnpj[2])*4+int(cnpj[3])*3+int(cnpj[4])*2+int(cnpj[5])*9+int(cnpj[6])*8+int(cnpj[7])*7+int(cnpj[8])*6+int(cnpj[9])*5+int(cnpj[10])*4+int(cnpj[11])*3+cnpj_digito_verificador_1*2 #etapa a
    resto=cnpj_digito_verificador_2%11 #etapa b
    if resto < 2: #etapa c
        cnpj_digito_verificador_2=0
    else:
        cnpj_digito_verificador_2=11-resto
    
    if cnpj[12]==str(cnpj_digito_verificador_1) and cnpj[13]==str(cnpj_digito_verificador_2):
        return True #cnpj valido
    else:
        return False #cnpj invalido

cnpj_teste='11222333000181'
print(conferir_cnpj(cnpj_teste))



