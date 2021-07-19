# -*- coding: cp1254 -*-
import random
mutasyonolasiligi = 0.01
def mutasyon(popilasyon):
    kopyapopilasyon=[]
    ############---KOPYALAMA------------------
    for i in range(0,len(popilasyon)):
        kopyapopilasyon.append([])
    for i in range(0,len(popilasyon)):
        for k in range(0,len(popilasyon[i])):
            kopyapopilasyon[i].append(popilasyon[i][k])
    #------------------------------------------------
            
    for i in range(0,len(kopyapopilasyon)):
        for k in range(0,len(kopyapopilasyon[i])):
            if(random.random()<=mutasyonolasiligi):
                #print "mutasyona ugradi"
                #print "onceki hali == ",kopyapopilasyon[i]
                #gen dublikasyonu yaptıralım canlinin genlerinin yarisi degissin yeni bir vcanlı ortaya cikmasi icin
                for h in range(0,len(kopyapopilasyon[i])/2):#kromozom sayının yarısı kadar gen değiştiricek
                    mutasyonnokta=random.randint(0,len(kopyapopilasyon[i])-1)
                    kopyapopilasyon[i][mutasyonnokta]=random.uniform(-1,1)

                #print "sonraki hali == ",kopyapopilasyon[i]
                

    return kopyapopilasyon
