# Datei öffnen
datei = open("fuhrpark.txt", "a+")

# Datei schreiben
eingabe = input("Welches Auto soll hinzugefügt werden? (Mehrere Autos bitte per Komma trennen) ")
einzelne_autos = eingabe.split (",")

# Aus
for i in einzelne_autos:
    datei.write("\n" + i)

datei.close