import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os
import re
from datetime import datetime

######Importando os Dados
#### Locais
dataD00="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Domicilios/"                                #Arquivos de Domicilios
dataP00="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Pessoas/"                                   #Arquivos de Pessoas

####Arquivos
D00=os.listdir(dataD00)                  #Lista de arquivos no diretorio
r=re.compile(".*Domicilios")             #Elementro de Regex- Arquivos Filtrados
D00=list(filter(r.match,D00))            
P00=os.listdir(dataP00)                  #Lista de arquivos no diretorio 
r=re.compile(".*Pessoas")                #Elementro de Regex- Arquivos Filtrados
P00=list(filter(r.match,P00))

#####DataFrame
####Domicilios
j=1
data_Dom=[]                              # Vetor contendo dataframes
for i in D00:
    globals()["Domicilios"+str(j)]=pd.read_csv(dataD00+str(i)) #Variaveis com o vetr
    globals()["Domicilios"+str(j)][np.isnan( globals()["Domicilios"+str(j)])]=0
    data_Dom.append(globals()["Domicilios"+str(j)])
    j=j+1 

####Pessoas
data_Pes=[]
for i in P00:
    globals()["Pessoas"+str(j)]=pd.read_csv(dataP00+str(i))
    globals()["Pessoas"+str(j)][np.isnan(globals()["Pessoas"+str(j)])]=0
    data_Pes.append(globals()["Pessoas"+str(j)])
    
    j=j+1


#######Saúde
#####Lixo
dic_Lixo=[]
i=0
for j in data_Dom:
    Lixo=j["V0212"]
    Lixob=pd.get_dummies(Lixo)
    Lixob=Lixob[1.0]+Lixob[2.0]
    dic_Lixo.append(Lixob)
    i=i+1
#####Esgoto
dic_Esgoto=[]
i=0
for j in data_Dom:
    Esgoto=j["V0211"]
    Esgotob=pd.get_dummies(Esgoto)
    Esgotob=Esgotob[1.0]
    dic_Esgoto.append(Esgotob)
    i=i+1
#########Situação do Domicilio
#####Água
dic_Agua=[]
i=0
for j in data_Dom:
    Agua=j["V0207"]
    Aguab=pd.get_dummies(Agua)
    Aguab=Aguab[1.0]+Aguab[2.0]+Aguab[3.0]
    dic_Agua.append(Aguab)
    i=i+1
#####Iluminação
dic_Iluminação=[]
i=0
for j in data_Dom:
    Iluminação=j["V0213"]
    Iluminaçãob=pd.get_dummies(Iluminação)
    Iluminaçãob=Iluminaçãob[1.0]
    dic_Iluminação.append(Iluminaçãob)
    i=i+1
#####Banheiros
dic_Banheiros=[]
i=0
for j in data_Dom:
    Banheiros=j["V0209"]
    Banheirosbin=pd.get_dummies(Banheiros)
    Colunas=Banheirosbin.columns.values
    Banheirosb=[0]*len(Banheirosbin[0.0])
    for k in Colunas:
        if k > 0:
            Banheirosb=Banheirosb+Banheirosbin[k]
    dic_Banheiros.append(Banheirosb)
    i=i+1

#####Item domesticos
#####Geladeira
dic_Geladeira=[]
ni=0
for j in data_Dom:
    Geladeira=j["V0215"]
    Geladeirab=pd.get_dummies(Geladeira)
    Geladeirab=Geladeirab[1.0]
    dic_Geladeira.append(Geladeirab)
    i=i+1
######Radio
dic_Radio=[]
i=0
for j in data_Dom:
    Radio=j["V0214"]
    Radiob=pd.get_dummies(Radio)
    Radiob=Radiob[1.0]
    dic_Radio.append(Radiob)
    i=i+1
#####Telefone
dic_Telefone=[]
i=0
for j in data_Dom:
    Telefone=j["V0219"]
    Telefoneb=pd.get_dummies(Telefone)
    Telefoneb=Telefoneb[1.0]
    dic_Telefone.append(Telefoneb)
    i=i+1
#####Automoveis
dic_Automoveis=[]
i=0
for j in data_Dom:
    Automoveis=j["V0222"]
    Automoveisbin=pd.get_dummies(Automoveis)
    Colunas=Automoveisbin.columns.values
    Automoveisb=[0]*len(Automoveisbin[0.0])
    for k in Colunas:
        if k > 0 :
            Automoveisb=Automoveisb+Automoveisbin[k]
    dic_Automoveis.append(Automoveisb)
    i=i+1
#####Condições
dic_Condições=[]
i=0
for j in data_Dom:
    Condições=j["V0205"]
    Condiçõesb=pd.get_dummies(Condições)
    Condiçõesb=Condiçõesb[1.0]+Condiçõesb[2.0]
    dic_Condições.append(Condiçõesb)
    i=i+1
#####Dormitorios per capita
dic_Dormitorios=[]
i=0
for j in data_Dom:
    Pessoas=j['V0110']+j['V0111']
    Dormitorios=Pessoas/j['V0204']
    Dormitoriosbin=pd.get_dummies(Dormitorios)
    Colunas=Dormitoriosbin.columns.values
    Dormitoriosb=[0]*len(Dormitoriosbin[1.0])
    for k in Colunas:
        if k < 2.00001:
            Dormitoriosb=Dormitoriosb+Dormitoriosbin[k]
    dic_Dormitorios.append(Dormitoriosb)
    i=i+1
#######Educação
######Escolaridade
dic_Escolaridade=[]
i=0
for j in data_Pes:
    Escolaridade=j.filter(items=['V4300','V0300'])
    Domicilio=j['V0300']
    Colunas=Domicilio.value_counts(sort=False).index
    Escolaridadeb=[]
    for k in Colunas:
        Controle=Escolaridade[Escolaridade['V0300']==k]
        num=[]
        for i in Controle['V4300']:
            if i>=20:
                num.append(0)
            elif i<=7:
                num.append(0)
            else:
                num.append(1)
        if np.mean(num)>=0:
            Escolaridadeb.append(1)
        else:
            Escolaridadeb.append(0)
    
    dic_Escolaridade.append(Escolaridadeb)
    i=i+1


########Frequencia
dic_Frequencia=[]
i=0
for j in data_Pes:
    Frequencia=j.filter(items=["V0628","V0300"])
    Domicilio=j["V0300"]
    Colunas=Domicilio.value_counts(sort=False).index
    Frequenciab=[]
    for k in Colunas:
        Controle=Frequencia[Frequencia['V0300']==k]
        num=[]
        for i in Controle['V0300']:
            if i==4:
                num.append(0)
            else:
                num.append(1)
        if np.mean(num) > 0:
            Frequenciab.append(1)
        else:
            Frequenciab.append(0)

    dic_Frequencia.append(Frequenciab)
    i=i+1

#########Renda
dic_Renda=[]
i=0
for j in data_Pes:
    Renda =j.filter(items=['V4615','V0300'])
    Domicilios=Renda['V0300']
    Colunas=Domicilios.value_counts(sort=False).index
    Rendab=[]
    for k in Colunas:
        Controle=Renda[Renda['V0300']==k]
        renda=np.mean(Controle['V4615'])
        if renda < 0.5 :
            Rendab.append(0)
        else:
            Rendab.append(1)

    dic_Renda.append(Rendab)
    i=i+1

########Tabelas IPM

Nomes=[Renda,Frequencia,Esgoto,Lixo,Agua,Iluminação,Banheiros,Geladeira,Radio,Telefone,Automoveis,Condições,Dormitorios,Renda]
Estados_2000=["AC","AP","AM","AL","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RN","RS","RJ","RO","RR","SC","SP","SE","TO"]
j=0
a=Renda
for i in range(0,len(data_Pes)):
    lista={"Renda":dic_Renda[i],"Frequencia":dic_Frequencia[i],"Escolaridade":dic_Escolaridade[i],"Esgoto":dic_Esgoto[i],"Lixo":dic_Lixo[i],"Agua":dic_Agua[i],"Iluminação":dic_Iluminação[i],"Banheiros":dic_Banheiros[i],"Geladeira":dic_Geladeira[i],"Radio":dic_Radimo[i],"Telefone":dic_Telefone[i],"Automoveis":dic_Automoveis[i],"Condições":dic_Condições[i],"Dormitorios":dic_Dormitorios[i]}
    data=pd.DataFrame(lista)
    data2=data_Dom[i].filter(items=['V0102', 'V1002', 'V1003', 'V0103', 'V0104', 'V0105','V0300', 'V0400', 'V1004', 'AREAP', 'V1001', 'V1005', 'V1006'])
    data2=data2.join(data)
    data2.to_csv("/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/IPM/"+str(Estados_2000[i])+".csv")


