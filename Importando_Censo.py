from urllib.request import urlretrieve
import pandas as pd
import tempfile
import zipfile
import os

########## Download dos dados do censo ############
#######Censo 2000
#####Estados
#AC="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/AC.zip"
#AP="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/AP.zip"
#AM="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/AM.zip"
#AL="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/AL.zip"
#BA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/BA.zip"
CE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/CE.zip"
#DF="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/DF.zip"
#ES="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/ES.zip"
#GO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/GO.zip"
#MA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/MA.zip"
#MT="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/MT.zip"
#MS="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/MS.zip"
#MG="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/MG.zip"
#PA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/PA.zip"
#PB="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/PB.zip"
#PR="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/PR.zip"
#PE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/PE.zip"
#PI="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/PI.zip"
#RN="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/RN.zip"
#RS="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/RS.zip"
#RJ="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/RJ.zip"
#RO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/RO.zip"
#RR="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/RR.zip"
#SC="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/SC.zip"
#SP="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/SP.zip"
#SE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/SE.zip"
#TO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2000/Microdados/TO.zip"
#Estados_2000=[AC,AP,AM,AL,BA,CE,DF,ES,GO,MA,MT,MS,MG,PA,PB,PR,PE,PI,RN,RS,RJ,RO,RR,SC,SP,SE,TO]
Estados_2000=[CE]
#####Censo 2010
#AC="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/AC.zip"
#AP="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/AP.zip"
#AM="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/AM.zip"
#AL="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/AL.zip"
#BA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/BA.zip"
CE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/CE.zip"
#DF="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/DF.zip"
#ES="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/ES.zip"
#GO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/GO.zip"
#MA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/MA.zip"
#MT="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/MT.zip"
#MS="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/MS.zip"
#MG="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/MG.zip"
#PA="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/PA.zip"
#PB="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/PB.zip"
#PR="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/PR.zip"
#PE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/PE.zip"
#PI="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/PI.zip"
#RN="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/RN.zip"
#RS="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/RS.zip"
#RJ="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/RJ.zip"
#RO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/RR.zip"
#SC="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/SC.zip"
#SP="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/SP.zip"
#SE="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/SE.zip"
#TO="ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Resultados_Gerais_da_Amostra/Microdados/TO.zip"
#Estados_2010=[AC,AP,AM,AL,BA,CE,DF,ES,GO,MA,MT,MS,MG,PA,PB,PR,PE,PI,RN,RS,RJ,RO,RR,SC,SP,SE,TO]
Estados_2010=[CE]
################ Fazendo Download
######Censo 2000
diretorios2000=[]
for i in Estados_2000 :
    local=tempfile.mktemp(suffix="2000.zip")     #Gerando diretorio aleatorio 
    diretorios2000.append(local)                 

j=0
for i in Estados_2000:
    local=diretorios2000[j]                      
    print(local)
    urlretrieve(i,filename=str(local))           #Fazendo download do arquivo contido no diretorio
    j=j+1
    print("Completo")
        
#####Censo2010
diretorios2010=[]
for i in Estados_2010:
    local=tempfile.mktemp(suffix="2010.zip")     #Gerando diretorio aleatorio
    diretorios2010.append(local)

j=0
for i in Estados_2010:
    local=diretorios2010[j]
    print(local)
    urlretrieve(i,filename=str(local))           #Fazerndo Download do arquivo contido no diretorio 
    j=j+1
    print("Completo")

######### Extraindo
#####Censo2000
for i in diretorios2000:
    zip=zipfile.ZipFile(i)                       #Criando um objeto tipo "zipfile"
    zip.extractall("/tmp/2000")                  #Extraindo o arquivo tipo "zipfile"

#####Censo2010
for i in diretorios2010:
    zip=zipfile.ZipFile(i)                       #Criando um objeto tipo "zipfile"
    zip.extractall("/tmp/2010")                  #Extraindo o arquivo tipo "zipfile"

########Criando os Paineis
#####Censo2000
####Separando arquivos
locais=os.listdir("/tmp/2000/")                  #Arquivos do diretorio temporari
j=0
arquivos1=[]                                     #Lista dos dados por pessoas
arquivos2=[]                                     #Lista dos dados por familias
arquivos3=[]                                     #Lista dos dados por domicilios
local_a=[]                                       #Diretorio dos Estados 
for i in locais:
    cantos=os.listdir("/tmp/2000/"+str(i))       #Arquivos dos diretorio por Estado 
    local="/tmp/2000/"+str(i)+"/"                #Local dos arquivos secundarios por Estado
    local_a.append(local)
    globals()[i+"P00"]=cantos[0]                   #Variaveis dinamicas para arquivos de Pessoas
    arquivos1.append(globals()[i+"P00"])
    
    globals()[i+"F00"]=cantos[1]                   #Variaveis dinamicas para arquivos de Familias
    arquivos2.append(globals()[i+"F00"])
    globals()[i+"D00"]=cantos[2]                   #Variaveis dinamicas para arquivos de Docimicilos
    arquivos3.append(globals()[i+"D00"])

#####Censo 2010
locais1=os.listdir("/tmp/2010/")                 #Arquivos do diretorio temporarios
j=0
arquivos4=[]                                     #Lista dos dados por pessoas
arquivos5=[]                                     #Lista dos dados por familias
arquivos6=[]                                     #Lista dos dados por domicilios
local_b=[]                                       #Diretorio dos Estados
for i in locais1:
    cantos=os.listdir("/tmp/2010/"+str(i))       #Arquivos dos diretorios por Estado
    local="/tmp/2010/"+str(i)+"/"                #Local dos arquivos secundarios por Estado
    local_b.append(local)
    globals()[i+"P10"]=cantos[0]                 #Variaveis dinamicas para arquivos de Pessoas
    arquivos4.append(globals()[i+"P10"])
    globals()[i+"F10"]=cantos[1]                 #Variaveis dinamicas para arquivos de Familias
    arquivos5.append(globals()[i+"F10"])
    globals()[i+"D10"]=cantos[3]                 #Variaveis dinamicas para arquivos de Domicilios 
    arquivos6.append(globals()[i+"D10"])
    


#######Leitura dos Dados
####Pessoas
largura=[2,4,5,7,9,11,8,2,2,13,1,1,1,1,1,1,2,2,1,3,2,1,1,3,1,1,1,1,1,1,2,1,1,1,4,2,2,2,1,7,2,7,1,1,2,1,1,2,1,2,2,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,1,6,6,6,1,6,6,6,6,6,2,2,3,1,1,6,6,6,6,6,6,6,2,2,2,2,2,11,2,2,2,2,2,2,1,2,2,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Nomes=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1004","AREAP","V1001","V1005","V1006","V1007","MARCA","V0401","V0402","V0403","V0404","V4752","V4754","V4070","V0408","V4090","V0410","V0411","V0412","V0413","V0414","V0415","V0416","V0417","V0418","V0419","V0420","V4210","V0422","V4230","V0424","V4250","V4260","V4276","V0428","V0429","V0430","V0431","V0432","V0433","V0434","V4355","V4300","V0436","V0437","V0438","V0439","V0440","V0441","V0442","V0443","V0444","V4452","V4462","V0447","V0448","V0449","V0450","V4511","V4512","V4513","V4514","V4521","V4522","V4523","V4524","V4525","V4526","V0453","V0454","V4534","V0455","V0456","V4573","V4583","V4593","V4603","V4613","V4614","V4615","V4620","V0463","V4654","V4670","V4690","P001","ESTR","ESTRP","V4621","V4622","V4631","V4632","V0464","V4671","V4672","V4354","V4219","V4239","V4269","V4279","V4451","V4461","M0401","M0402","M0403","M0404","M4752","M4754","M0408","M4090","M0410","M0411","M0412","M0413","M0414","M0415","M0416","M0417","M0418","M0419","M0420","M4210","M0422","M4230","M0424","M4250","M4260","M4276","M0428","M0429","M0430","M0431","M0432","M0433","M0434","M4355","M0436","M0437","M0438","M0439","M0440","M0441","M0442","M0443","M0444","M4452","M4462","M0447","M0448","M0449","M0450","M4511","M4512","M4521","M4522","M0453","M0454","M0455","M0456","M4573","M4583","M4593","M4603","M4613","M4620","M4654","M4670","M0463","M4621","M4622","M4631","M4632","M0464","M4671","M4672"]

###Censo 2000
destino="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Pessoas/"
j=0
for i in arquivos1:
    variavel=str(local_a[j])+str(i)
    a=pd.read_fwf(variavel,colspecs=None,widths=largura, names=Nomes)
    a.to_csv(destino+str(i)+".csv",sep=",")
    j=j+1

###Censo 2010
largura=[2,5,13,8,3,1,2,3,2,1,2,2,1,3,3,2,1,1,1,1,1,1,1,1,1,1,4,1,7,7,3,3,1,7,7,7,1,7,7,7,1,1,2,2,1,1,2,1,1,1,3,3,3,1,7,7,7,1,2,1,1,1,1,1,1,1,4,5,1,1,1,1,6,6,4,1,6,4,7,4,7,4,7,5,6,4,3,1,1,1,1,1,1,6,1,7,7,7,1,1,1,2,2,2,1,2,2,2,1,3,1,1,1,2,4,1,2,2,2,2,1,2,1,1,1,1,1,3,1,2,2,2,6,4,4,5,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Nomes=["V0001","V0002","V0011","V0300","V0010","V1001","V1002","V1003","V1004","V1006 ","V0502","V0504","V0601","V6033","V6036","V6037","V6040","V0606","V0613","V0614","V0615","V0616","V0617","V0618","V0619","V0620","V0621","V0622","V6222","V6224","V0623","V0624","V0625","V6252","V6254","V6256","V0626","V6262","V6264","V6266","V0627","V0628","V0629","V0630","V0631","V0632","V0633","V0634","V0635","V6400","V6352","V6354","V6356","V0636","V6362","V6364","V6366","V0637","V0638","V0639","V0640","V0641","V0642","V0643","V0644","V0645","V6461","V6471","V0648","V0649","V0650","V0651","V6511","V6513","V6514","V0652","V6521","V6524","V6525","V6526","V6527","V6528","V6529","V6530","V6531","V6532","V0653","V0654","V0655","V0656","V0657","V0658","V0659","V6591","V0660","V6602","V6604","V6606","V0661","V0662","V0663","V6631","V6632","V6633","V0664","V6641","V6642","V6643","V0665","V6660","V6664","V0667","V0668","V6681","V6682","V0669","V6691","V6692","V6693","V6800","V0670","V0671","V6900","V6910","V6920","V6930","V6940","V6121","V0604","V0605","V5020","V5060","V5070","V5080","V6462","V6472","V5110","V5120","V5030","V5040","V5090","V5100","V5130","M0502","M0601","M6033","M0606","M0613","M0614","M0615","M0616","M0617","M0618","M0619","M0620","M0621","M0622","M6222","M6224","M0623","M0624","M0625","M6252","M6254","M6256","M0626","M6262","M6264","M6266","M0627","M0628","M0629","M0630","M0631","M0632","M0633","M0634","M0635","M6352","M6354","M6356","M0636","M6362","M6364","M6366","M0637","M0638","M0639","M0640","M0641","M0642","M0643","M0644","M0645","M6461","M6471","M0648","M0649","M0650","M0651","M6511","M0652","M6521","M0653","M0654","M0655","M0656","M0657","M0658","M0659","M6591","M0660","M6602","M6604","M6606","M0661","M0662","M0663","M6631","M6632","M6633","M0664","M6641","M6642","M6643","M0665","M6660","M0667","M0668","M6681","M6682","M0669","M6691","M6692","M6693","M0670","M0671","M6800","M6121","M0604","M0605","M6462","M6472","V1005"]
o
destino="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Pessoas/"
j=0
for i in arquivos4:
    variavel=str(local_b[j])+str(i)
    a=pd.read_fwf(variavel,colspecs=None,widths=largura,names=Nomes)
    a.to_csv(destino+str(i)+".csv",sep=",")
    j=j
    +1

#######Domicilios
#####Censo 2000
Nomes=["V0102","V1002","V1003","V0103","V0104","V0105","V0300","V0400","V1001","V1004","AREAP","V1005","V1006","V1007","V0110","V0111","V0201","M0201","V0202","M0202","V0203","M0203","V0204","M0204","V0205","M0205","V0206","M0206","V0207","M0207","V0208","M0208","V0209","M0209","V0210","M0210","V0211","M0211","V0212","M0212","V0213","M0213","V0214","M0214","V0215","M0215","V0216","M0216","V0217","M0217","V0218","M0218","V0219","M0219","V0220","M0220","V0221","M0221","V0222","M0222","V0223","M0223","V7100","V7203","V7204","V7401","V7402","V7403","V7404","V7405","V7406","V7407","V7408","V7409","V7616","V7617","P001","V1111","V1112","V1113"]

largura=[2,4,5,7,9,11,8,2,1,2,13,1,1,1,2,2,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,2,2,2,2,2,2,2,2,2,6,6,11,1,1,1]

destino="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Domicilios/"
j=0
for i in arquivos3:
    variavel=str(local_a[j])+str(i)
    a=pd.read_fwf(variavel,widths=largura,names=Nomes)
    a.to_csv(destino+str(i)+".csv")
    j=j+1

#####Censo2010
largura=[2,5,13,8,3,1,2,3,2,1,2,2,1,6,4,1,2,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,7,5,6,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
Nomes=["V0001","V0002","V0011","V0300","V0010","V1001","V1002","V1003","V1004","V1006","V4001","V4002","V0201","V2011","V2012","V0202","V0203","V6203","V0204","V6204","V0205","V0206","V0207","V0208","V0209","V0210","V0211","V0212","V0213","V0214","V0215","V0216","V0217","V0218","V0219","V0220","V0221","V0222","V0301","V0401","V0402","V0701","V6529","V6530","V6531","V6532","V6600","V6210","M0201","M2011","M0202","M0203","M0204","M0205","M0206","M0207","M0208","M0209","M0210","M0211","M0212","M0213","M0214","M0215","M0216","M0217","M0218","M0219","M0220","M0221","M0222","M0301","M0401","M0402","M0701","V1005"]

destino="/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Domicilios/"
j=0
for i in arquivos6:
    variavel=str(local_b[j])+str(i)
    a=pd.read_fwf(variavel,widths=largura,names=Nomes)
    a.to_csv(destino+str(i)+".csv")
    j=j+1

