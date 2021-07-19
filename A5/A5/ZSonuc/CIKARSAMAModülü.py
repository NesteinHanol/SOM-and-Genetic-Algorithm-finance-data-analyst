# -*- coding: cp1254 -*-

import VeriModeliOkuma
denemegirdi=VeriModeliOkuma.Liste()

for i in range(0,len(denemegirdi)):
    for k in range(0,len(denemegirdi[i])-1):#sondaki tarihi almamak için
        denemegirdi[i][k]=float(denemegirdi[i][k])

#--------------------------------------------------------------------------
import WagirlikOkuma
W=WagirlikOkuma.Liste()

for i in range(0,len(W)):
    for k in range(0,len(W[i])):
        W[i][k]=float(W[i][k])

hucresayisi=100
gparamssayisi=len(denemegirdi[0])-1
testvektorsayisi=len(denemegirdi)

#--------------------------------------------------------------------------------
hucreveri=[]
for i in range(0,hucresayisi):
    hucreveri.append([])

toplam=0
mindizibul=[]
import math
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
    hucreveri[indes].append(denemegirdi[s][len(denemegirdi[s])-1])
    #print s,"-",denemegirdi[s] ," == ", indes
    mindizibul=[]
    toplam=0  

#-------------------------TEST KISMI ------------------------------------
denemegirdiTest=VeriModeliOkuma.TestListe()
for i in range(0,len(denemegirdiTest)):
    for k in range(0,len(denemegirdiTest[i])-1):
        denemegirdiTest[i][k]=float(denemegirdiTest[i][k])

gparamssayisi=len(denemegirdiTest[0])-1
testvektorsayisi=len(denemegirdiTest)

for s in range(0,testvektorsayisi):#testvektor sayisi
    for l in range(0,hucresayisi):
        for i in range(0,gparamssayisi):
            toplam=toplam+(denemegirdiTest[s][i]-W[i][l])**2
        mindizibul.append(math.sqrt(toplam))
    #print ("mindizibul[",l,"]","==",math.sqrt(toplam))
        toplam=0

    enk=999999999999999999
    mind=list(mindizibul)
    for i in range(0,len(mindizibul)):
        if mindizibul[i] < enk:
            enk=mindizibul[i]
            indes=i
    hucreveri[indes].append(denemegirdiTest[s][len(denemegirdiTest[s])-1])
    mindizibul=[]
    toplam=0
    
for i in range(0,len(hucreveri[indes])):
    print i ," --- ",hucreveri[indes][i] 
