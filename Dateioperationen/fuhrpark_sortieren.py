# Datei öffnen
datei = open("fuhrpark.txt", "r")

# Inhalt der Datei lesen
inhalt = datei.read()
datei.close()
# Inhalt zu Luste umkonvertieren
alle_zeilen = inhalt.split()

#Liste sortieren
alle_zeilen.sort()

# neue Datei öffnen
datei_sortiert = open ("fuhrpark_sortiert.txt", "w")

# sortierten Inhalt in datei schreiben
for i in alle_zeilen:
    datei_sortiert.write(i + "\n")

# neue Datei schließen
datei_sortiert.close()

# Ausgabe der sortierten Liste
for i in alle_zeilen:
    print(i)