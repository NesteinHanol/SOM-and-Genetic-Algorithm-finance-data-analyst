# -*- coding: cp1254 -*-
x=-1
uzaklik=[]
W=[]
##for i in range(0,100):
##  uzaklik.append([])
import math
import random

##for i in range(0,10):#10x10 kare yapinin birbirleri ile olan uzakliklarini bulma
##  for k in range(0,10):
##    x=x+1
##    for s in range(0,10):
##      for l in range(0,10):
##        z=math.sqrt((i-s)**2+(k-l)**2)
##        uzaklik[x].append(z)
xduzlemihucresayisi=20
yduzlemihucresayisi=20

a=[]

x=0

for i in range(0,xduzlemihucresayisi):
    a.append([x,0])
    x=x+3**(0.5)
    
b=[]
c=0.5*3**(0.5)
for i in range(0,xduzlemihucresayisi):
    b.append([c,1.5])
    c=c+3**(0.5)

e=[]
e.append(list(a))
s=[]
for i in range(1,xduzlemihucresayisi/2):
    for k in range(0,xduzlemihucresayisi):
        s.append([e[i-1][k][0],e[i-1][k][1]+3])

    e.append(list(s))
    s=[]

ee=[]
ee.append(list(b))
ss=[]
for i in range(1,xduzlemihucresayisi/2):
    for k in range(0,xduzlemihucresayisi):
        ss.append([ee[i-1][k][0],ee[i-1][k][1]+3])
    
    ee.append(list(ss))
    ss=[]

dx=[]
for i in range(0,xduzlemihucresayisi/2):
    dx.append(list(e[i]))
    dx.append(list(ee[i]))

uzaklik=[]
for i in range(0,xduzlemihucresayisi*yduzlemihucresayisi):
  uzaklik.append([])

x=-1

for i in range(0,xduzlemihucresayisi):#10x10 kare yapinin birbirleri ile olan uzakliklarini bulma
  for k in range(0,xduzlemihucresayisi):
    x=x+1
    for s in range(0,xduzlemihucresayisi):
      for l in range(0,xduzlemihucresayisi):
        z=math.sqrt((dx[i][k][0]-dx[s][l][0])**2+(dx[i][k][1]-dx[s][l][1])**2)
        #z=math.sqrt((i-s)**2+(k-l)**2)
        uzaklik[x].append(z)

#---------------------FİNANCE GİRDİ --------------------------------
import VeriModeliOkuma
denemegirdi=VeriModeliOkuma.Liste()

for i in range(0,len(denemegirdi)):
    for k in range(0,len(denemegirdi[i])-1):#sondaki tarihi almamak için
        denemegirdi[i][k]=float(denemegirdi[i][k])
#--------------------------------------------------------------------

hucresayisi=xduzlemihucresayisi*yduzlemihucresayisi #10x10 luk haritada 100 olur değiştirmeyi unutmna otomatikleştirmek şart.
gparamssayisi=len(denemegirdi[0])-1
testvektorsayisi=len(denemegirdi)

#--------------------W agirlik ayarlama----------------------------------------------------

for i in range(0,gparamssayisi):#girdi sayisi kadar
  W.append([])

for i in range(0,gparamssayisi):#agirliklari olusturma
  for k in range(0,hucresayisi):
    W[i].append(random.uniform(0.001,1))

#-------------------------------------------------------
    
W1=[]
po=0.1
T2=10000.0
go=(xduzlemihucresayisi+yduzlemihucresayisi)/2.0#n+m nxm matrisli yapinin degeri
T1=10000.0/math.log(go)
#T1=99.0
W1=list( W[0])
W2=list(W[1])
##ONEMLI BIR SONUC 1000 İTERASYON SAYISI YUKARDA T1 VE T2 Yİ ETKİLEMELİ    
for n in range(0,10000):
  print n,"---------"
  mindizibul=[]
  toplam=0
  g=go*math.exp(-n/T1)
  p=po*math.exp(-n/T2)
  for s in range(0,testvektorsayisi):#testvektor sayisi
    for l in range(0,hucresayisi):
      for i in range(0,gparamssayisi):
        toplam=toplam+(denemegirdi[s][i]-W[i][l])**2
      mindizibul.append(math.sqrt(toplam))# girdinin hucrelere karsı olan uzaklıgı bulunur
      
      toplam=0

    enk=999999999999999999
    mind=list(mindizibul)
    for i in range(0,len(mindizibul)):#en yakın ücre bulunur
      if mindizibul[i] < enk:
        enk=mindizibul[i]
        indes=i
     #print indes
    #print indes
    mindizibul=[]
    toplam=0
    
  ##Egitim Kismi
    for v in range(0,hucresayisi):
      h=math.exp((-uzaklik[indes][v])/(2.0*(g**2.0)))
      for w in range(0,gparamssayisi):
        W[w][v]=W[w][v]+p*h*(denemegirdi[s][w]-W[w][v])

##    for w in range(0,60):
##      W[w][indes]=W[w][indes]+p*(denemegirdi[s][w]-W[w][indes])
  #print p       
#-------------------------------END --------------------------------------

#-----------------W(agirlik) Matrisini Dosyaya yazma-----------------------------
dosya=open("W1.txt","w")
st=""
for i in range(0,len(W)):
    for k in range(0,len(W[i])-1):
        st=st+str(W[i][k])+","
    st=st+str(W[i][len(W[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()
#--------------------------------------------------------------------------------
dosya=open("sonuc1D-10000-01.txt","w")
st=""
for s in range(0,testvektorsayisi):#testvektor sayisi
    for l in range(0,hucresayisi):
        for i in range(0,gparamssayisi):
            toplam=toplam+(denemegirdi[s][i]-W[i][l])**2
        mindizibul.append(math.sqrt(toplam))
    #print ("mindizibul[",l,"]","==",math.sqrt(toplam))
        toplam=0

    enk=999999999999999999
    mind=list(mindizibul)
    for i in range(0,len(mindizibul)):
        if mindizibul[i] < enk:
            enk=mindizibul[i]
            indes=i
    #print indes
    #print indes
    #print s,"-",denemegirdi[s] ," == ", indes
    st=str(s)+"-"+str(denemegirdi[s])+" == "+str(indes)
    st=st+"\n"
    dosya.write(st)
    st=""
    mindizibul=[]
    toplam=0     

dosya.close()












