from urllib.request import urlretrieve
from unicodedata import normalize
import shutil
import tempfile
import zipfile
import os


##########Download Mapas
#########Download dos mapas #######
######2000
###Estados
AC="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ac/ac_municipios.zip"
AP="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ap/ap_municipios.zip"
#AM="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/am/am_municipios.zip"
#AL="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/al/al_municipios.zip"
#BA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ba/ba_municipios.zip"
#CE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ce/ce_municipios.zip"
#DF="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/df/df_municipios.zip"
#ES="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/es_municipios.zip"
#GO="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/go/go_municipios.zip"
#MA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ma/ma_municipios.zip"
#MT="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/mt/mt_municipios.zip"
#MS="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ms/ms_municipios.zip"
#MG="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/mg/mg_municipios.zip"
#PA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/pa/pa_municipios.zip"
#PB="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/pb/pb_municipios.zip"
#PR="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/pr/pr_municipios.zip"
#PE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/pe/pe_municipios.zip"
#PI="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/pi/pi_municipios.zip"
#RN="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/rn/rn_municipios.zip"
#RS="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/rs/rs_municipios.zip"
#RJ="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/rj/rj_municipios.zip"
#RO="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/ro/ro_municipios.zip"
#RR="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/rr/rr_municipios.zip"
#SC="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/sc/sc_municipios.zip"
#SP="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/sp/sp_municipios.zip"
#SE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/se/se_municipios.zip"
#TO="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2000/to/to_municipios.zip"
#Estados_2000=[AC,AP,AM,AL,BA,CE,DF,ES,GO,MA,MT,MS,MG,PA,PB,PR,PE,PI,RN,RS,RJ,RO,RR,SC,SP,SE,TO]
Estados_2000=[AC,AP]

#######Censo2010
AC="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ac/ac_municipios.zip"
AP="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ap/ap_municipios.zip"
#AM="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/am/am_municipios.zip"
#AL="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/al/al_municipios.zip"
#BA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ba/ba_municipios.zip"
#CE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ce/ce_municipios.zip"
#DF="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/df/df_municipios.zip"
#ES="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/es_municipios.zip"
#GO="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/go/go_municipios.zip"
#MA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ma/ma_municipios.zip"
#MT="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/mt/mt_municipios.zip"
#MS="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ms/ms_municipios.zip"
#MG="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/mg/mg_municipios.zip"
#PA="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/pa/pa_municipios.zip"
#PB="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/pb/pb_municipios.zip"
#PR="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/pr/pr_municipios.zip"
#PE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/pe/pe_municipios.zip"
#PI="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/pi/pi_municipios.zip"
#RN="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/rn/rn_municipios.zip"
#RS="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/rs/rs_municipios.zip"
#RJ="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/rj/rj_municipios.zip"
#R0="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/ro/ro_municipios.zip"
#RR="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/rr/rr_municipios.zip"
#SC="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/sc/sc_municipios.zip"
#SP="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/sp/sp_municipios.zip"
#SE="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/se/se_municipios.zip"
#TO="ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2010/to/to_municipios.zip"
#Estados_2010=[AC,AP,AM,AL,BA,CE,DF,ES,GO,MA,MT,MS,MG,PA,PB,PR,PE,PI,RN,RS,RJ,RO,RR,SC,SP,SE,TO]
Estados_2010=[AC,AP]
#########Fazendo download
######Censo2000
diretorios2000=[]
for i in Estados_2000:
    local=tempfile.mktemp(suffix="mapa2000.zip")
    diretorios2000.append(local)

j=0
for i in Estados_2000:
    local=diretorios2000[j]
    print(local)
    urlretrieve(i,filename=str(local))
    j=j+1
    print("Completo")

######Censo2010
diretorios2010=[]
for i in Estados_2010:
    local=tempfile.mktemp(suffix="mapa2010.zip")
    diretorios2010.append(local)
j=0
for i in Estados_2010:
    local=diretorios2010[j]
    print(local)
    urlretrieve(i,filename=str(local))
    j=j+1
    print("Completo")

#########Extraindo
#####Censo2000
for i in diretorios2000:
    zip=zipfile.ZipFile(i)
    zip.extractall("/tmp/2000")

#####Censo2010
for i in diretorios2010:
    zip=zipfile.ZipFile(i)
    zip.extractall("/tmp/2010")



########Criando os Paineis
######Censo2000
locais2000=os.listdir("/tmp/2000/")
locais2010=os.listdir("/tmp/2010/")

#######Codificando os Arquivos
######Censo2000)
acento=[]
for i in locais2000:
  a=open(i,'w',encoding='utf-8')
  b=a.write("/tmp/2000/"+str(i))
  a.close()
#####Movendo arquivos

#####Censo2000
for i in locais2000:
    shutil.move("/tmp/2000/"+str(i),"/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2000/Mapas/"+str(i))

#####Censo2010
for i in locais2010:
    shutil.move("/tmp/2010/"+str(i),"/home/alexandre/Documentos/IPECE/Pobreza-Multidimensional/Censo/2010/Mapas/"+str(i))



