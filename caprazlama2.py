# -*- coding: cp1254 -*-
#sansa ba�l� olmayan caprazlama anneden ve babadan e�it say�da dna gelir
def Caprazla2(indes1,indes2,popilasyon):
    #print dizi
    #print dizi2
    #dizi=[1,2,3,4,5,6,7,8,9,12,3,4,5,6]
    #dizi2=[44,33,11,77,55,44,33,88,77,99,445,654,323,54]

    import random

    dizi3=[]
    dizi4=[]

    #dizi3 i�in
    secim=0
    for i in range(0,len(popilasyon[indes1])):
        if (i/2== i/2.0):
            dizi3.append(popilasyon[indes1][i])
            
        else:
            dizi3.append(popilasyon[indes2][i])

    #dizi4 i�in #sadece bir �aprazlamadan bir �ocuk oldu�unu varsay�yoruz
##    for i in range(0,len(dizi2)):
##        secim=random.randrange(2)
##        if (secim == 0):
##            dizi4.append(dizi[i])
##        else:
##            dizi4.append(dizi2[i])

    return dizi3
#dizi1 ve dizi2 kendiyle bir se�ilimde en fazla 4 kere �aprazlanmal�
#yeni jenerasyon olu�tuktan sonra dizi1 ve dizi2 silinmeli

