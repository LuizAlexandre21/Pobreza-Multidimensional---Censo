import pandas as pd
import numpy as np
import os


######Variaveis do Censo
#####2000
###Educação
#V4300 - Pessoas- Escolaridade
#V0429 - Pessoas- Frequencia Escolar
###Saúde
#V0211 - Domicilios- Esgoto
#V0212 - Domicilios- Lixo
###Situação Do Domicilios
#V0207 - Domicilios - Água
#V0213 - Domicilios - Iluminação
#V0209 - Domicilios - Banheiro
#V0215 & V0214 & V0219 & V0222 - Domicilios - Itens Domesticos
#V0205 - Domicilios - Condição do Domicilio
#V0110 & V0111 & V0204 - Dormitorios per capita
###Renda
#V4614 -Pessoas - Rendimentos
#####2010
###Educação
#V0633 - Pessoas - Escolaridade
#V0628 - Pessoas - Frequencia
###Saúde
#V0210 - Domicilios - Lixo
#V0207 - Domicilios - Esgoto
###Condição do Domicilios
#V0208 - Domicilios - Água
#V0211 - Domicilios - Iluminação
#V0205 - Domicilios - Banheiro 
#V0213 & V0214 & V0217 & V0218 & V0222 - Domicilios- Itens Domesticos
#V0201 - Domicilios - Condição do Domicilio
#V6204 - Domicilios - Dormitorios per capita
###Renda
#V6527 - Pessoas - Rendimentos


#######Importando os Dados
localD00="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Domicilios/"
localP00="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Pessoas/"
localD10="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Domicilios/"
localP10="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Pessoas/"

Domi2000=os.listdir(localD00)
Pess2000=os.listdir(localP00)
Domi2010=os.listdir(localD10)
Pess2010=os.listdir(localP10)

j=0
for i in Domi2000:
    data=pd.read_csv(localD00+i)
    data=data.filter(items=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1004","AREAP","V1001","V1005","V1006","V0421","V0211","V0212","V0207","V0213","V0209","V0215","V0214","V0219","V0222","V0205","V0110","V0111","V0204","V4615"])
    data.to_csv(localD00+"Domicilios"+str(j)+".csv")
    j=j+1
    
for i in Domi2010:
    data1=pd.read_csv(localD10+i)
    data1=data.filter(items=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1004","AREAP","V1001","V1005","V1006","V0210","V0207","V0209","V0211","V0213","V0214","V0217","V0218","V0222","V0201","V6204","V0205"])
    data1.to_csv(localD10+"Domicilios"+str(j)+".csv")
    j=j+1
    
for i in Pess2000:
    data=pd.read_csv(localP00+i)
    data=data.filter(items=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1004","AREAP","V1001","V1005","V1006","V4300","V0429","V4614","V4615"])
    data.to_csv(localP00+"Pessoas"+str(j)+".csv")
    j=j+1
    
for i in Pess2010:
    data=pd.read_csv(localP10+i)
    data=data.filter(items=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1004","AREAP","V1001","V1005","V1006","V6527","V0633","V0628"])
    data.to_csv(localP10+"Pessoas"+str(j)+".csv")
    j=j+1








