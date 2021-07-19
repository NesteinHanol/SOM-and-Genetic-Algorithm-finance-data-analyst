# -*- coding: cp1254 -*-
dosya = open("eurusdALL.txt")
x=dosya.readlines()
t=len(x)
k=[]
gun5=[]
gun15=[]
gun20=[]
veri=[]
#dosya.seek(0)#imleci basa goturuyor dosyayi yeniden okuyabilmek icin
for i in range(0,t):
    #print(dosya.read())
    k.append(x[i].split())

for h in range(0,len(k),5):
    veri.append([k[h][0],float(k[h][5]),float(k[h+1][5]),float(k[h+2][5]),float(k[h+3][5]),float(k[h+4][5])])   


#----------------------------------------------------------------------------
p=[]
for i in range(t-1,-1,-1):
    p.append(x[i].split())

m5=[]
m10=[]
#m15=[]
m20=[]
toplam=0
##for i in range(0,5):
##    toplam=toplam+float(p[i][1])
##    
##m5.append([p[4][0],toplam/5])    

for i in range(0,t-4):#t normal degerden bir fazla oldugu için -4 yapılır -5 değil
    for s in range(0,5):
        toplam=toplam+float(p[i+s][1])
    m5.append([p[i+s][0],toplam/5])
    toplam=0

for i in range(0,t-9):
    for s in range(0,10):
        toplam=toplam+float(p[i+s][1])
    
    m10.append([p[i+s][0],toplam/10])
    toplam=0

##for i in range(0,t-14):
##    for s in range(0,15):
##        toplam=toplam+float(p[i+s][1])
##    m15.append([p[i+s][0],toplam/15])
##    toplam=0

for i in range(0,t-19):
    for s in range(0,20):
        toplam=toplam+float(p[i+s][1])
    m20.append([p[i+s][0],toplam/20])
    toplam=0

veri2=[]
stori=[]        
for i in range(19,len(k)):#[tarih,%degisim,kapanıs,m5,m10,m15,m20]
    for g in range(0,len(m5)):
        if p[i][0]==m5[g][0]:
            #veri2.append([p[i][0],float(p[i][1]),m5[g][1]])
            stori.append(p[i][0])
            stori.append(float(p[i][5]))#yüzdelik değişim
            stori.append(float(p[i][1]))#kapanis fiyati
            stori.append(m5[g][1])
    #for g in range(0,len(m10)):
    for g in range(0,len(m10)):
        if p[i][0]==m10[g][0]:
            stori.append(m10[g][1])

##    for g in range(0,len(m15)):           
##        if p[i][0]==m15[g][0]:
##            stori.append(m15[g][1])

    for g in range(0,len(m20)):
        if p[i][0]==m20[g][0]:
            stori.append(m20[g][1])
    veri2.append(list(stori))
    stori=[]

veri3=[]
for i in range(0,len(veri2)): 
    veri3.append(list(veri2[i]))

for i in range(0,len(veri2)):#[tarih,%degisim,kapanıs,m5-k%,m10-k%,m15-k%,m20-k%]
    deger=veri2[i][3]-veri2[i][2]#m5-k
    yzd = (100.0*deger)/veri2[i][2]
    veri3[i][3]=yzd
    
    deger=veri2[i][4]-veri2[i][2]#m10-k
    yzd = (100.0*deger)/veri2[i][2]
    veri3[i][4]=yzd

##    deger=veri2[i][5]-veri2[i][2]#m15-k
##    yzd = (100.0*deger)/veri2[i][2]
##    veri3[i][5]=yzd

    deger=veri2[i][5]-veri2[i][2]#m20-k
    yzd = (100.0*deger)/veri2[i][2]
    veri3[i][5]=yzd
    
#[tarih,%degisim,kapanıs,m5,m10,m15,m20]
for i in range(0,len(veri2)):
    deger=veri2[i][3]-veri2[i][4] #m5-m10 
    yzd=(100.0*deger)/veri2[i][3]
    veri3[i].append(yzd)
    
##    deger=veri2[i][3]-veri2[i][5]#m5-m15
##    yzd=(100.0*deger)/veri2[i][3]
##    veri3[i].append(yzd)

    deger=veri2[i][3]-veri2[i][5]#m5-m20
    yzd=(100.0*deger)/veri2[i][3]
    veri3[i].append(yzd)

##    deger=veri2[i][4]-veri2[i][5]#m10-m15
##    yzd=(100.0*deger)/veri2[i][4]
##    veri3[i].append(yzd)

    deger=veri2[i][4]-veri2[i][5]#m10-m20
    yzd=(100.0*deger)/veri2[i][4]
    veri3[i].append(yzd)

##    deger=veri2[i][5]-veri2[i][6]#m15-m20
##    yzd=(100.0*deger)/veri2[i][5]
##    veri3[i].append(yzd)

for i in range(0,len(veri3)):
    veri3[i].pop(2)

#kaç gün aralığını alıcaksak burada belirtiyoruz şuanlık 5 günlük aralık alınıcak
#o yüzden benzetimaralik == 1 olarak aliniyor 
veri4=[]
benzetimaralik=1
for i in range(0,len(veri3),benzetimaralik):
    veri4.append([veri3[i][0]])

for i in range(0,len(veri3)):
    veri3[i].pop(0) #tarihi baştan çıkarıyor 
    veri3[i].append(veri3[i][0])#yüzdelik değişimi yeniden eklemek için
    veri3[i].append(veri3[i][0])#yüzdelik değişimi yeniden eklemek için
d=0   
for i in range(0,len(veri3),benzetimaralik):
    for k in range(0,benzetimaralik):
        if (i==len(x)-20 and k==1):#20 son aldığımız aralık olduğu için burda -20 demek lazım
            break
        else:
            for t in range(0,len(veri3[i+k])):
                veri4[d].append(veri3[i+k][t])
    d=d+1

for i in range(0,len(veri4)):#tarihi sona eklemek
    deger=veri4[i][0]
    veri4[i].pop(0)
    veri4[i].append(deger)

veri4.pop(len(veri4)-1)

dosya=open("veri1.txt","w")
st=""
for i in range(0,len(veri4)):
    for k in range(0,len(veri4[i])-1):
        st=st+str(veri4[i][k])+","
    st=st+str(veri4[i][len(veri4[i])-1])
    st=st+"\n"
    dosya.write(st)
    st=""
dosya.close()

    
