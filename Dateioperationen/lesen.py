# Datei öffnen
datei = open("fuhrpark.txt", "r")

# kompletten Inhalt der Datei in eine Variable lesen
inhalt = datei.read()
# einzelne Zeilen in Liste schreiben
inhalt = inhalt.split()

# über Liste iterieren und Inhalt zeilenweise ausgeben
laenge = len(inhalt)
for i in range(laenge):
    print(i+1, inhalt[i])

# Datei schließen
datei.close()