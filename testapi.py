# -*- coding: cp1254 -*-

import secilim
##import caprazlama
import caprazlama2
import mutasyon
import PopilasyonOlusturma
import habidatOlusturma
import SinirAgiHesapla
##import random

popilasyonsayisi=1
popilasyonIndex=[]
#popilasyonIndex=[[0,110],[1,120],[2,99],[3,35]]#index and fitenss
popilasyonA=[]
eylemkayit=[]
for i in range(0,popilasyonsayisi):
    popilasyonIndex.append([i,0])#100 bakiyeyi temsil ediyor

girdiSiniragi1=[7,3,2]#ilk katman için

#popilasyonA=PopilasyonOlusturma.olustur(girdiSiniragi1,popilasyonsayisi)
#popilasyonA=[[-0.061595926797627376, 0.3096041343975513, 0.6471550636975056, 0.69088589640252, -0.32819001320384933, -0.6302217734389763, 0.9602396300707399, -0.7790864958687942, 0.5331490426638155, 0.9051145325930108, 0.017606728593312804, 0.502304201637898, 0.5310276461680503, -0.002778387739115873, 0.6041351027253246, 0.7715403634935447, 0.5259964411137708, 0.9917462165957676, 0.1608022084903331, 0.8834866364150371, -0.869563415340799, 0.7222676892808855, 0.7098456736971417, 0.1602455876178812, -0.4170944293433858, -0.16343599845950885, -0.7872797900519306, -0.8688592618552147, 0.3342917860676742, -0.7851306925750032, 0.6765350479476862, -0.0860488793709735, 0.19882149280845907]]

#[7,3,2] egitim.txt
#popilasyonA=[[-0.47330676581105413, 0.020373722194958255, 0.3498894864602906, 0.39247690845735783, 0.6803819300588061, 0.8719799497865157, 0.604380157867616, 0.23877386817508328, 0.2173082290936441, 0.29115435201232964, 0.1454121494175229, 0.12399280410105074, -0.04069291069507708, -0.8323854681931917, -0.96241375066763, -0.9591212207957069, -0.8278824245990788, 0.33165106129336674, -0.7304029459050541, 0.05904716080257533, -0.7504324041216728, 0.6835733970179962, -0.6299195694554709, -0.7139736343435816, -0.22043921746530026, 0.9858209136637262, 0.17447971708424492]]

popilasyonA=[[-0.27491147466868004, -0.8893612640959019, -0.19381558837262536, 0.4467002426295441, -0.5894625047294386, -0.7289423664520425, -0.9622250538786219, 0.9013939036941176, 0.4105089625083962, 0.8947524268626026, 0.30384140891322575, -0.12588243763451823, 0.29727922532912543, -0.987801508835239, -0.0025032958635493596, 0.39938587462554986, 0.5105089857776972, 0.16773413691861094, -0.09323433822512861, -0.804240510034784, 0.6930595032714624, -0.3154519931070674, -0.12671186126130962, 0.8018620272639576, 0.3664517560962275, 0.6607750797821716, -0.3061316542284107]]






habidat=[]
habidat=habidatOlusturma.habidatolustur("test4.txt")#dosya ismi degistirme unutma

jSayac=0
jenerasyonSayisi=1
while (jSayac < jenerasyonSayisi ) :
    for i in range(0,len(popilasyonIndex)):
        HesapKromozomRenk="N"
        for k in range(0,len(habidat)-girdiSiniragi1[0]+1):
            girdi=[]
            for s in range(k,k+girdiSiniragi1[0]-1):
                girdi.append((float(habidat[s][len(habidat[s])-1])))
            if HesapKromozomRenk=="N":#nötür ne yeşil ne kırmızı
                girdi.append(0)
            elif HesapKromozomRenk=="Y":
                girdi.append(0.5)
                deger=len(girdi)-2
                popilasyonIndex[i][1]=popilasyonIndex[i][1]+(100*girdi[deger]/100)
            elif HesapKromozomRenk=="K":
                girdi.append(-0.5)
                deger=len(girdi)-2
                popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*girdi[deger]/100)

            
            for rr in range(0,1):

                eylem=SinirAgiHesapla.siniragihesapla(girdi,popilasyonA[i],"A",girdiSiniragi1)

                if jSayac == jenerasyonSayisi-1 :
                    eylemkayit.append([eylem,habidat[k+girdiSiniragi1[0]-2],"--",popilasyonIndex[i][1]])

                if eylem=="Y":
                    if HesapKromozomRenk=="K":#renk degistirme maliyeti ekle
                        popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*1/100)# %1 komisyon k
                    HesapKromozomRenk="Y"
                elif eylem=="K":
                    if HesapKromozomRenk=="Y":#renk degistirme maliyeti ekle
                        popilasyonIndex[i][1]=popilasyonIndex[i][1]-(100*1/100)# %1 komi
                    HesapKromozomRenk="K"

    jSayac=jSayac+1
    print "0000000000000000000000000"
for i in range(0,len(eylemkayit)):
    print eylemkayit[i]

print "-------------",popilasyonIndex



    
