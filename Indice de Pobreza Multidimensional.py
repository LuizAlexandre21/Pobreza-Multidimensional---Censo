
import pandas as pd
import numpy as np
import scipy as sc
import unicodedata
import os
import matplotlib.pyplot as plt
import matplotlib.cm
import re
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

#######Funções
####Indice de Pobreza Multidimensional - IPM
def IPM(dados):
    dim=dados.shape                      #Dimensão dos Dados 
    col=range(0,dim[1])                  #Lista de colunas 
    dados.columns=col                    #Trocando os nomes por numeros
    dados[np.isnan(dados)]=0             #Trocando dados nulos por 0 
    IPM=[0]                               
    for i in col:                 
        n=IPM[i]+dados[i]                #Somando os resultados das colunas      
        IPM.append(n)                 
    pov=(1/dim[1])*IPM[dim[1]]           #IPM=media ponderada 
    return pov                           #Indice de pobreza por linha

#######Censo 2000
#####Importando os Dados

dados="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/IPM/"
diretorio=sorted(os.listdir(dados))
data=[]
j=0
for i in diretorio:
    globals()["data"+str(j)]=pd.read_csv(dados+i)
    data.append(globals()["data"+str(j)])
    j=j+1

########Subindices de Pobreza
#####Saúde
Variaveis=[]
j=0
for i in data:
    #######Saúde 
    saude=i.filter(items=["Esgoto","Lixo"])
    IPMS=IPM(saude)
    #######Saúde 
    Condições=i.filter(items=["Agua","Iluminação","Banheiros","Geladeira","Radio","Telefone","Dormitorios","Automoveis","Condições"])
    IPMC=IPM(Condições)
    #######Educação
    Educação=i.filter(items=["Frequencia","Escolaridade"])
    IPME=IPM(Educação)
    #######Renda
    IPMR=i['Renda']
    Geral=i.filter(items=["Esgoto","Lixo","Agua","Iluminação","Banheiros","Geladeira","Radio","Telefone","Dormitorios","Automoveis","Condições","Frequencia","Escolaridade","Renda"])
    IPMG=IPM(Geral)
    dic={"IPMS":IPMS,"IPME":IPME,"IPMC":IPMC,"IPMR":IPMR,"IPMG":IPMG}
    globals()["Estado"+str(j)]=pd.DataFrame(dic)
    globals()["Estado"+str(j)]=globals()["Estado"+str(j)].join(i.filter(items=['V0102', 'V1002', 'V1003', 'V0103', 'V0104', 'V0105','V0300', 'V0400', 'V1004', 'AREAP', 'V1001', 'V1005', 'V1006']))
    globals()["Estado"+str(j)].to_csv("IPMDATA"+str(j)+".csv")
    Variaveis.append(globals()["Estado" + str(j)])
    j=j+1

######Gerando Indices
dado=[]
for i in Variaveis:
    Variavel=i
    Coluna=Variavel['V0103'].value_counts(sort=False).index
    IPMG=[]
    IPME=[]
    IPMC=[]
    IPMR=[]
    IPMS=[]
    for k in Coluna:
        Controle=Variavel[Variavel['V0103']==k]
        IPMG.append(Controle['IPMG'].mean())
        IPME.append(Controle['IPME'].mean())
        IPMC.append(Controle['IPMC'].mean())
        IPMR.append(Controle['IPMR'].mean())
        IPMS.append(Controle['IPMS'].mean())
    dicmun={"IPMG":IPMG,"IPME":IPME,"IPMC":IPMC,"IPMR":IPMR,"IPMS":IPMS}
    data=pd.DataFrame(dicmun)
    a=Variavel.filter(items=['V0102', 'V1002', 'V1003', 'V0103', 'V0104', 'V0105','V0300', 'V0400', 'V1004', 'AREAP', 'V1001', 'V1005', 'V1006'])
    data.join(a)
    dado.append(data)
    
    
######Graficos
########Importando as Cordenadas
coordenadas=pd.read_csv("/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/Lat-Lon.csv")
Estados=['Acre','Amapá']
########Lista de Shapefiles
Shapefiles=os.listdir("/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Mapas")
r=re.compile(".*shp")
shp=list(filter(r.match,Shapefiles))
shp=sorted(shp)
#####Criando Mapas
j=0
for i in Estados:
    fig,ax=plt.subplots(figsize=(10,20))
    coordenadasa=coordenadas[i]
    m=Basemap(resolution='i',projection='merc',lat_0=coordenadasa[4:5],lon_0=coordenadasa[5:6],llcrnrlon=coordenadasa[0:1],llcrnrlat=coordenadasa[1:2],urcrnrlon=coordenadasa[2:3],urcrnrlat=coordenadasa[3:4])
    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
    m.drawcoastlines()
    loc=shp[j].replace(".shp","")
    m.readshapefile('/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Mapas/'+str(loc),'areas')
    datamap=pd.DataFrame({'shape':[Polygon(np.array(shape),True) for shape in m.areas],'area':[areas['CODIGO'] for areas in m.areas_info]})
    datamap=datamap.join(dado[j])
    cmap=plt.get_cmap('Oranges')
    pc=PatchCollection(datamap['shape'],zorder=2)
    norm=Normalize()
    pc.set_facecolor(cmap(norm(datamap['IPMG'].fillna(0).values)))
    ax.add_collection(pc)
    mapper=matplotlib.cm.ScalarMappable(norm=norm,cmap=cmap)
    mapper.set_array(datamap['IPMG'])
    plt.colorbar(mapper,shrink=0.4)
    plt.title("Indice de Pobreza Multidimensional -"+str(i))
    plt.show()
    j=j+1
