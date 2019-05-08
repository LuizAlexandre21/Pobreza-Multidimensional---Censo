import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import os
import re
from datetime import datetime
start=datetime.now()

####Importando os Dados
dataD10="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Domicilios/"
dataP10="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Pessoas/"

####Arquivos
D10=os.listdir(dataD10)
r=re.compile(".*Domicilios")
D10=list(filter(r.match,D10))
P10=os.listdir(dataP10)
r=re.compile(".*Pessoas")
P10=list(filter(r.match,P10))

######DataFrame
####Domicilios
j=1
data_Dom=[]
for i in D10:
    globals()["Domicilios"+str(j)]=pd.read_csv(dataD10+str(i))
    #globals()["Domicilios"+str(j)][np.isnan(globals()["Domicilios"+str(j)])]==0
    data_Dom.append(globals()["Domicilios"+str(j)])
    j=j+1
####Pessoas
data_Pes=[]
j=1
for i in P10:
    globals()["Pessoas"+str(j)]=pd.read_csv(dataP10+str(i))
    #globals()["Pessoas"+str(j)][np.isnan(globals()["Pessoas"+str(j)])]=0
    data_Pes.append(globals()["Pessoas"+str(j)])
    j=j+1

########Saude
#####Lixo
dic_Lixo=[]
i=0
for j in data_Dom:
    Lixo=j["V0210"]
    Lixob=pd.get_dummies(Lixo)
    Lixob=Lixob[1.0]+Lixo[2.0]
    dic_Lixo.append(Lixob)
    i=i+1

####Esgoto
dic_Esgoto=[]
i=0
for j in data_Dom:
    Esgoto=j["V0207"]
    Esgotob=pd.get_dummies(Esgoto)
    Esgotob=Esgotob[0.0]
    dic_Esgoto.append(Esgotob)
    i=i+1

########Situação do Domicilio
#####Agua
dic_Agua=[]
i=0
for j in data_Dom:
    Agua=j["V0209"]
    Aguab=pd.get_dummies(Agua)
    Aguab=Aguab[1.0]
    dic_Agua.append(Aguab)
    i=i+1

######Iluminação
dic_Iluminação=[]
i=0
for j in data_Dom:
    Iluminação=j["V0211"]
    Iluminaçãob=pd.get_dummies(Iluminação)
    Iluminaçãob=Iluminaçãob[1.0]+Iluminaçãob[2.0]
    dic_Iluminação.append(Iluminaçãob)
    i=i+1

######Banheiros
dic_Banheiros=[]
i=0
for j in data_Dom:
    Banheiros=j["V0205"]
    Banheirosbin=pd.get_dummies(Banheiros)
    Colunas=Banheirosbin.columns.values
    Banheirosb=[0]*len(Banheirosbin[0.0])
    for k in Colunas:
        if k > 0:
            Banheirosb=Banheirosb+Banheirosbin[k]
    dic_Banheiros.append(Banheirosb)
    i=i+1
    
######Itens Domesticos
####Radio
dic_Radio=[]
i=0
for j in data_Dom:
    Radio=j["V0213"]
    Radiob=pd.get_dummies(Radio)
    Radiob=Radiob[1.0]
    dic_Radio.append(Radiob)
    i=i+1
    
#####Televisão
dic_Televisão=[]
i=0
for j in data_Dom:
    Televisão=j["V0214"]
    Televisãob=pd.get_dummies(Televisão)
    Televisãob=Televisãob[1.0]
    dic_Televisão.append(Televisãob)
    i=i+1

######Celular
dic_Celular=[]
i=0
for j in data_Dom:
    Celular=j["V0217"]
    Celularb=pd.get_dummies(Celular)
    Celularb=Celular[1.0]
    dic_Celular.append(Celularb)
    i=i+1


######Telefone
dic_Telefone=[]
i=0
for j in data_Dom:
    Telefone=j["V0218"]
    Telefoneb=pd.get_dummies(Telefone)
    Telefoneb=Telefoneb[1.0]
    dic_Telefone.append(Telefoneb)
    i=i+1

#######Automovel
dic_Automoveis=[]
i=0
for j in data_Dom:
    Automovel=j["V0222"]
    Automovelb=pd.get_dummies(Automovel)
    Automovelb=Automovel[1.0]
    dic_Automoveis.append(Automovel)
    i=i+1


########Condições
#dic_Condicões=[]
#i=0
#for j in data_Dom:
#    Condições=j["V0201"]
#    Condiçõesb=pd.get_dummies(Condições)
#    dic_Condicões.append(Condiçõesb)
#    i=i+1

########Dormitoriosb per capita
dic_Dormitorios=[]
i=0
for j in data_Dom:
    Dormitorios=j["V6204"]
    Dormitoriosbin=pd.get_dummies(Dormitorios)
    Colunas=Dormitoriosbin.columns.values
    Dormitoriosb=Dormitorios[0]*len(Dormitoriosbin[0.0])
    for k in Colunas:
        if k <2.000000001:
            Dormitoriosb=Dormitoriosb+Dormitoriosbin[k]
    dic_Dormitorios.append(Dormitoriosb)
    i=i+1

##########Educação
#########Escolaridade
dic_Escolaridade=[]
i=0
for j in data_Pes:
    Escolaridade=j.filter(items=["V0633","V0300"])
    Domicilios=j["V0300"]
    Colunas=Domicilios.value_counts(sort=False).index
    Escolaridadeb=[]
    for k in Colunas:
        Controle=Escolaridade[Escolaridade['V0300']==k]
        num=[]
        for i in Controle['V0633']:
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


#########Frequencia
dic_Frequencia=[]
i=0
for j in data_Pes:
    Frequencia=j.filter(items=["V0628","V0300"])
    num=[]
    for k in Colunas:
        Controle=Frequencia[Frequencia['V0300']==k]
        Frequenciab=[]
        for i in Controle['V0628']:
            if i==4:
                num.append(0)
            else:
                num.append(1)
        if np.mean(num)>0 :
            Frequenciab.append(1)
        else:
            Frequenciab.append(0)
            
    dic_Frequencia.append(Frequenciab)
    i=i+1

###########Renda
dic_Renda=[]
i=0
for j in data_Pes:
    Renda=j.filter(items=['V5080','V0300'])
    Domicilios=Renda['V0300']
    Colunas=Domicilios.value_counts(sort=False).index
    Rendab=[]
    for k in Colunas:
        Controle=Renda[Renda['V0300']==k]
        renda=np.mean(Controle['V5080'])
        if renda <0.5:
            Rendab.append(0)
        else:
            Rendab.append(1)

    dic_Renda.append(Rendab)
    i=i+1



Estados_2010=["AC","AP","AM","AL","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RN","RS","RJ","RO","RR","SC","SP","SE","TO"]
j=0
for i in range(0,len(data_Pes)):
    lista={"Renda":dic_Renda[i],"Frequencia":dic_Frequencia[i],"Escolaridade":dic_Escolaridade[i],"Esgoto":dic_Esgoto[i],"Lixo":dic_Lixo[i],"Agua":dic_Agua[i],"Iluminação":dic_Iluminação[i],"Banheiros":dic_Banheiros[i],"Radio":dic_Radio[i],"Televisão":dic_Televisão[i],"Celular":dic_Celular[i],"Telefone":dic_Telefone[i],"Automoveis":dic_Automoveis[i],"Dormitorios":dic_Dormitorios[i]}
    data=pd.DataFrame(lista)
    data2=data_Dom[i].filter(['V0102', 'V1002', 'V1003', 'V0103', 'V0104', 'V0105','V0300', 'V0400', 'V1004', 'AREAP', 'V1001', 'V1005', 'V1006'])
    data2=data2.join(data)
    data2.to_csv("/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/IPM/"+str(Estados_2010[i])+".csv")


















print(datetime.now()-start)
