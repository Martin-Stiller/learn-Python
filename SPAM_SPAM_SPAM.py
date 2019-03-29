
# Modul random importieren mit funktion shuffle 
from random import shuffle

# eine liste mit Wörtern , mit ".upper()" alle Wörter in der Liste groß schreiben,
# mit .split() jedes wort als variable deklarieren "amazing" "gorgeous"...
liste=("amazing gorgeous vibrant blazing stunning biggest fastest tremendous fantastic phenomenal delightful \
ambitious staggering  smarter massive incredible spectacular super excited cool magical revolutionary intuitive").upper().split()

# Die liste mischen
shuffle(liste)

# 5 Strophen
for strophe in range(5):
    # 2 Zeilen SPAM SPAM
    for zeile in range(2):
        # Schleife für SPAM SPAM SPAM SPAM mit ",end=''" wir der Zeilenumbruch verhindert  
        for spam in range(4):
            print("Spam ",end='')
        print()
        # print ("SPAM"*4)würde auch gehen und spart die schleife
        print ("SPAM "*4)
        
# ausgabe vom inhalt der liste und "SPAM", keines der Wörter darf zweimal vorkommen.
# Zwei Variablen festlegen die jeweils ein Wort aus der liste nehmen und aus der Liste löschen. 
# "liste.pop(0)" hier nehme ich das 0te wort also wort 1 und nehme es aus der liste
    ele1 = liste.pop(0)
    ele2 = liste.pop(1)
 
 # Ausgabe der letzten Zeile {} dienen als platzhalter für ele1 und ele2 die mit .format(ele1, ele2) am ende angegebn werden
    print("{} SPAM , {} SPAM".format(ele1, ele2))
    print()
 
