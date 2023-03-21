# neues Auto: Volvo! muss mit in den Fuhrpark aufgenommen werden

# Datei öffnen
datei = open("fuhrpark.txt", "a+")

# Datei schreiben
inhalt = "\nVolvo"
datei.write(inhalt)

inhalt = "\nFiat"
datei.write(inhalt)

datei.close
