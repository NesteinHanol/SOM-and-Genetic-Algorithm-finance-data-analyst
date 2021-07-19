# -*- coding: cp1254 -*-
import random
import math
import HesapDiziCevir
##def sigmoid(x):
##  return 1 / (1 + math.exp(-x))
def tanh(x):
  return math.tanh(x)

def siniragihesapla(girdi,diziG,HesapKromozomRenk,girdiSiniragi):
  #veri=[34,11,92,6,7]
  dizi=HesapDiziCevir.hesapdizicevir(girdiSiniragi,diziG)
  if (type(HesapKromozomRenk) == str):
    veri = girdi[:]
    toplam=0
    veri2=[]
    for i in range(0,len(dizi)):
        for k in range(0,len(dizi[i])):
            for s in range(0,len(dizi[i][k])):
                toplam=toplam+dizi[i][k][s]*veri[s]
                #print str(k) ," + ",str(dizi[i][k][s])," * ",str(veri[s])

            #sonuc=sigmoid(toplam)
            sonuc=tanh(toplam)
            #print "---" ,toplam
            #sonuc=toplam
            toplam=0
            veri2.append(sonuc)
        #print veri2 , "----------------"
        #print "girdi = ", girdi
        #print "dizi = " ,dizi
        #print "sonuc = ", veri2
        #print "-----------------------------------"
        veri=[]
        veri=veri2[:]
        veri2=[]

    if(veri[0]>=veri[1]):
      return "Y"
    if(veri[1]>=veri[0]):
      return "K"


