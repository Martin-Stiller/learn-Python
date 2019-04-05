
# Definiere eine Funktion get_temp()
def get_temp():
    # Beginne schleife  
    while True:
        # Usereingabe
        C = input("bitte Temperatur in Celsius angeben: ")
        # prüfe ob die eingabe eien Zahl (flieskomma) ist 
        try:
            C = float(C)
            # wenn es eine zahl ist gib die Zahl zurück
            return C
            # ist die Zahl keine Zahl und es erscheint
            # der Fehler ValueError
        except ValueError:
            # gib diese Fehlermeldung aus
            # und wiederhole die Schleife
            print ("das ist keine Gültige eingabe")
# Definiere die Umrechnung von Kelvin nach °C
# das Ergebinis ist die Variable "C" , "K" wird nur innerhalb der 
# Definition zum rechnen benutzt!
def convert_to_kelvin(C):
    # berechne das Ergebnis        
    K = C + 237.15
    # und gib es zurück
    return K 

# Programmeinstieg
if __name__ == "__main__":
    # definiere die Variable C mit der get_temp Definition
    C = get_temp()
    # wenn def_temp C zurückgibt  verwandle die variable C
    # in einen string , berechne C mit der Definition convert_to_kelvin
    # und gib das dann aus
    print("die Temperatur in Kelvin beträgt: " + str(convert_to_kelvin(C)))      
