# -*- coding: cp1254 -*-
#rank secilimi DENEYSEL
#tumdizi=[[0.2,0.2,0.3,110],[0.44,0.2321,0.443,120],[0.4,0.9,0.7,99],[0.4,0.9,0.7,35]]
import random
#import caprazlama
#popilasyonIndex=[[0,110],[1,120],[2,99],[3,35]]#index and fitenss
def secilim(popilasyonIndex):
    tumdizi=popilasyonIndex[:]
    yenitumdizi=[]
    enk=9999999999999999999999
    for k in range(0,len(tumdizi)):
        for i in range(k,len(tumdizi)):
            if(tumdizi[i][len(tumdizi[i])-1] < enk):
                enk = tumdizi[i][len(tumdizi[i])-1]
                indis=i

        enk=9999999999999999999999999
        tasinacak=tumdizi[k]
        tumdizi[k]=tumdizi[indis]
        tumdizi[indis]=tasinacak
        
    for i in range(0,len(tumdizi)):
        tumdizi[i][len(tumdizi[i])-1]=i+1

    oran = (len(tumdizi)*(len(tumdizi)+1))/2.0
    toplam=0
    for i in range(0,len(tumdizi)):#secilme olsasiliklari  atama
        tumdizi[i][len(tumdizi[i])-1]=tumdizi[i][len(tumdizi[i])-1]/oran
        
    for i in range(0,len(tumdizi)):#birikimli olasılık haline getirme
        toplam=toplam+tumdizi[i][len(tumdizi[i])-1]
        tumdizi[i][len(tumdizi[i])-1]=toplam

    #seçilme sıklığını belirtmen gerek farklı yaklaşımlar denenebilir
    yenidizi=[]
    anaKromozom=[]
    babaKromozom=[]
    sayac=0
    secilmisKromozomlar=[]
    while (sayac<len(tumdizi)):
        randomsayi = random.random()
        for c in range(0,len(tumdizi)):
            if(randomsayi <= tumdizi[c][len(tumdizi[c])-1]):
                anaKromozom=tumdizi[c]
                break
        randomsayi2 = random.random()
        for s in range(0,len(tumdizi)):
            if(randomsayi2 <= tumdizi[s][len(tumdizi[s])-1]):
                babaKromozom=tumdizi[s]
                break
        if (babaKromozom == anaKromozom):
            pass
        else:
            
            #del anaKromozom[len(anaKromozom)-1]
            #del babaKromozom[len(babaKromozom)-1]
            #yeniKromozom=caprazlama.Caprazla(anaKromozom,babaKromozom)#kromozom çaprazlama yapılıyor ama bu sefer ayrı olmaz ayırmak için mainde yapıcak
            #yenidizi.append(yeniKromozom)
            secilmisKromozomlar.append([anaKromozom,babaKromozom])
            
            sayac=sayac+1
            #print "anaKromozom = ",anaKromozom
            #print "babaKromozom = ",babaKromozom
            #print "----------------------------------------------"
    return secilmisKromozomlar    
