#!/usr/bin/python3.7
import matplotlib.pyplot as plt

summe = 0
feldliste = []

for felder in range(64):
    reiskorn = 2**felder
    feldliste.append(reiskorn)
    summe = summe + reiskorn
    print ("Feld {} = {:>30,} Reiskörner und damit insgesamt {:>30,} Reiskörner".format(felder+1,reiskorn,summe))

gewicht = summe * 0.02 / 1000 / 1000
print()
print ("Wenn ein Reiskorn 0.02g wiegt, wiegen alle Reiskörner {:,.0f} Tonnen".format(gewicht))
plt.plot(feldliste)
plt.show()
