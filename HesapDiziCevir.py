# -*- coding: cp1254 -*-

def hesapdizicevir(girdiSiniragi,islemdizi):
################################### Hesap dizisine çevirme
# sinir ağı değerleri hesaplanırken bu formata çevrilicek
    #girdi=[5,4,3,3]#sinir agi parametreleri
    hesapdizi=[]

    for i in range(0,len(girdiSiniragi)-1):
        hesapdizi.append([])
    for i in range(0,len(girdiSiniragi)-1):
        for k in range(0,girdiSiniragi[i+1]):
            hesapdizi[i].append([])

    indes=0
    for i in range(0,len(girdiSiniragi)-1):
        for k in range(0,len(hesapdizi[i])):
            for s in range(0,girdiSiniragi[i]):
                hesapdizi[i][k].append(islemdizi[indes])
                indes=indes+1
    return hesapdizi
