import VeriModeliOkuma
denemegirdi=VeriModeliOkuma.Liste()

for i in range(0,len(denemegirdi)):
    for k in range(0,len(denemegirdi[i])-1):
        denemegirdi[i][k]=float(denemegirdi[i][k])


denemegirdiTest=VeriModeliOkuma.TestListe()
for i in range(0,len(denemegirdiTest)):
    for k in range(0,len(denemegirdiTest[i])-1):
        denemegirdiTest[i][k]=float(denemegirdiTest[i][k])
