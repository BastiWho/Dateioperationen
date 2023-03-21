import os
import math

try: 
    # Datei öffnen zum schreiben
    datei = open ("text.txt", "x")

    # zu schreibender Text definieren
    text = "Hallo, dass ist ein einfacher Text."

    #text in datei schreiben
    datei.write (text)

    #datei schließen
    datei.close()

except FileExistsError:
    eingabe = input("Die Datei exestiert schon- soll ich die Löschen [J/N]?") 
    if eingabe.capitalize() == "J":
        os.remove("text.txt")
        print("Die Datei wurde gelöscht.")
        datei = open ("text.txt", "x")
        text = "Das ist ein neuer Text in der Datei."
        datei.write(text)
    else:
        print("Die Datei wurde nicht gelöscht")
except:
    print("Etwas ist schief gelaufen.")
finally:
    print("Das ist ja immer da!")
