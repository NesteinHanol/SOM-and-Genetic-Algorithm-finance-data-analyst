def olustur(girdi,popilasyonsayisi):
    import random
    carpim=1
    toplam=0
    for i in range(0,len(girdi)-1):
        carpim = girdi[i]*girdi[i+1]
        toplam=toplam+carpim
        
    popilasyonliste=[]

    for i in range(0,popilasyonsayisi):
        popilasyonliste.append([])

    for i in range(0,popilasyonsayisi):
        for k in range(0,toplam):
            popilasyonliste[i].append(random.uniform(-1,1))
            
    return popilasyonliste
    
