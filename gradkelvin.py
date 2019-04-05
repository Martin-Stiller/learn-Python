
# Definiere eine Funktion get_temp()

def get_temp():
    # beginne schliefe  
    while True:
        # Usereingabe
        C = input("bitte Temperatur in Celsius angeben: ")
        # prüfe ogb die eingabe eien Zahl ist 
        try:
            C = float(C)
            # wenn es eine zahl ist gib die Zahl zurück
            return C
            # ist dei zahl keine Zahl also es eischeint
            # der Fehler ValueError
        except ValueError:
            # gib diese Fehlermeldung aus
            print ("das ist keine Gültige eingabe")
# Definiere die umrechnung von Kelvin nach °C
# das ergebinis ist die Variable "C" , "K" wird nur innerhalb der 
# definition zum rechnen benutzt!
def convert_to_kelvin(C):
    # berechne das Ergebnis        
    K = C + 237.15
    # und gib es zurück
    return K 

# programmeinstieg
if __name__ == "__main__":
    # definiere die variable C mit der get_temp definition
    C = get_temp()
    # wenn def_temp C zurückgibt  verwandle die variable C
    # in einen string , berechne C mit der definition convert_to_kelvin
    # und gib das dann aus
    print("die Temperatur in Kelvin beträgt: " + str(convert_to_kelvin(C)))      
