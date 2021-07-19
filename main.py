# -*- coding: cp1254 -*-

import secilim
##import caprazlama
import caprazlama2
import mutasyon
import PopilasyonOlusturma
import habidatOlusturma
import SinirAgiHesapla
##import random

popilasyonsayisi=100
popilasyonIndex=[]
#popilasyonIndex=[[0,110],[1,120],[2,99],[3,35]]#index and fitenss
popilasyonA=[]
eylemkayit=[]
for i in range(0,popilasyonsayisi):
    popilasyonIndex.append([i,0])#100 bakiyeyi temsil ediyor

girdiSiniragi1=[7,3,2]#ilk katman için

popilasyonA=PopilasyonOlusturma.olustur(girdiSiniragi1,popilasyonsayisi)


habidat=[]
habidat=habidatOlusturma.habidatolustur("egitim2.txt")

jSayac=0
jenerasyonSayisi=100

while (jSayac <= jenerasyonSayisi ) :
    popilasyonIndex=[]
    for i in range(0,popilasyonsayisi):
        popilasyonIndex.append([i,0])#100 bakiyeyi temsil ediyor
    for i in range(0,len(popilasyonIndex)):
        HesapKromozomRenk="N"
        for k in range(0,len(habidat)-girdiSiniragi1[0]+1):
            girdi=[]
            for s in range(k,k+girdiSiniragi1[0]-1):# -1 çünkü sonda ki değeri yeşil yada kırmızı olarak olıcak -1,0,1
                girdi.append((float(habidat[s][len(habidat[s])-1])))#her zaman alinacak deger sonda olmalı
            if HesapKromozomRenk=="N":#nötür ne yeşil ne kırmızı
                girdi.append(0)
            elif HesapKromozomRenk=="Y":
                girdi.append(0.5)
                deger=len(girdi)-2

                popilasyonIndex[i][1]=popilasyonIndex[i][1]+(100*girdi[deger]/100)*10
                
            elif HesapKromozomRenk=="K":
                girdi.append(-0.5)
                deger=len(girdi)-2
                
                popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*girdi[deger]/100)*10
                
            for rr in range(0,1):
                
                eylem=SinirAgiHesapla.siniragihesapla(girdi,popilasyonA[i],"A",girdiSiniragi1)
                
                if jSayac == jenerasyonSayisi and i==enbindex:
                    #eylemkayit[i].append([eylem,habidat[k],girdi])
                    #print enbindex
                    eniyi=popilasyonA[enbindex]
                    eylemkayit.append([eylem,habidat[k+girdiSiniragi1[0]-2]])
                    
                #print eylem ," tarih = ", habidat[k]
                if eylem=="Y":
                    if HesapKromozomRenk=="K":#renk degistirme maliyeti ekle
                        popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*1/100)*10# %1 komisyon kesme
                    
                    HesapKromozomRenk="Y"
                elif eylem=="K":
                    if HesapKromozomRenk=="Y":#renk degistirme maliyeti ekle
                        popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*1/100)*10# %1 komisyon kesme
                        
                    HesapKromozomRenk="K"


    #print popilasyonIndex        
    toplamZ=0
    enbZ=-99999999999999
    for w in range(0,len(popilasyonIndex)):
        if(popilasyonIndex[w][1]>enbZ):
            enbZ=popilasyonIndex[w][1]
            enbindex=w
        toplamZ=toplamZ+popilasyonIndex[w][1]

    print jSayac,"--******************" , toplamZ/100.0 ,"en iyi =",enbZ
    #print popilasyonA[enbindex]
    #print popilasyonIndex
    if (jSayac != jenerasyonSayisi):#son degere geldiğinde tekrar seçilim çaprazlama yapmasını engellicek
        
        secilmisciftlerdizi=secilim.secilim(popilasyonIndex)
    
        caprazlanmisA=[]
        for i in range(0,len(secilmisciftlerdizi)):
            caprazlanmisA.append(caprazlama2.Caprazla2(secilmisciftlerdizi[i][0][0],secilmisciftlerdizi[i][1][0],popilasyonA))

        caprazlanmisA=mutasyon.mutasyon(caprazlanmisA)
##    
        popilasyonA=[]
        for i in range(0,len(caprazlanmisA)):#popilasyonA kopyalama kısmı
           popilasyonA.append([])
        for i in range(0,len(caprazlanmisA)):
            for k in range(0,len(caprazlanmisA[i])):
                popilasyonA[i].append(caprazlanmisA[i][k])

##    popilasyonIndex=[]
##    for i in range(0,popilasyonsayisi):
##        popilasyonIndex.append([i,0])#100 bakiyeyi temsil ediyor
        
    jSayac=jSayac+1
    
#for i in range(0,len(eylemkayit)):
#    print eylemkayit[i]
