# -*- coding: cp1254 -*-
def habidatolustur(dosyaadi):
    dosya=open(dosyaadi)
    x=dosya.readlines()
    t=len(x)
    k=[]

    for i in range(0,t):    
        k.append(x[i].split(","))

    for i in range(0,t): #sondaki /n i�aretini yok etmek ve sistemi satir haline getirmek i�in 
        x=k[i][len(k[0])-1].split()
        k[i][len(k[0])-1]=x[0]

#a�-y�ksek-d���k-kapan�i-hacim
    habidat=[]
    for i in range(0,len(k)):

        fark=float(k[i][5])-float(k[i][2])
        yuzdelikdegisim=(fark*100)/float(k[i][2])
        habidat.append([k[i][0]+"-"+k[i][1],yuzdelikdegisim])


        
##        if (yuzdelikdegisim>0):
##            habidat.append([k[i][0]+"-"+k[i][1],1.0])
##        if(yuzdelikdegisim<0):
##            habidat.append([k[i][0]+"-"+k[i][1],-1.0])
##        if(yuzdelikdegisim==0):
##            habidat.append([k[i][0]+"-"+k[i][1],0.0])

    #--MIN MAX NORMAL�ZASYONU girdi degerleri art�nca her skalar girdi i�in yap
##    enk=9999999999999999999
##    for i in range(0,len(habidat)):#-min(x) buluyor
##        if(habidat[i][1]<enk):
##            enk=habidat[i][1]
##    enb=-999999999999999
##    for i in range(0,len(habidat)):
##        if(habidat[i][1]>enb):
##            enb=habidat[i][1]
##        
##    for i in range(0,len(habidat)):#burda sadece son deger skaler o y�zden son eleman uygulan�r
##        habidat[i][1]=(habidat[i][1]-enk)/(enb-enk)
    
    return habidat
