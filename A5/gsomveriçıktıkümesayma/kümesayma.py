# -*- coding: cp1254 -*-
dosya=open("sonuc1D-10000-01.txt")
x=dosya.readlines()
t=len(x)
k=[]
for i in range(0,t):    
    k.append(x[i].split(" "))

for i in range(0,t): #sondaki /n işaretini yok etmek ve sistemi satir haline getirmek için 
    x=k[i][len(k[0])-1].split()
    k[i][len(k[0])-1]=x[0]

toplam=0
print ("-------- 511-10000.txt ---------")
for i in range(0,400):
    for s in range(0,t):
        if (int(k[s][len(k[0])-1])==i):
            toplam=toplam+1
    print (i," kumenin eleman sayisi == ",toplam)
    toplam=0

#Part-Time Blogger, Part-Time Engineer, Full-Time Dessert Lover, Obsessed With 80&90's.
