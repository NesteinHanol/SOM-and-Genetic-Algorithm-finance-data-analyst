# -*- coding: cp1254 -*-
def Liste():
    dosya=open("veri1.txt")
    x=dosya.readlines()
    t=len(x)
    k=[]
    for i in range(0,t):    
        k.append(x[i].split(","))

    for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
        x=k[i][len(k[0])-1].split()
        k[i][len(k[0])-1]=x[0]
        
    return k
