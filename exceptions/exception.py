zahl1 = input("Bitte erste Zahl angeben: ")
zahl2 = input("Bitte zweite Zahl angeben: ")

#Programm versucht ein Ergebnis zu errechnen.
try:
    ergebnis = int(zahl1) / int(zahl2)

#Wenn der User durch 0 teilt, erscheint folgende Ausgabe
except ZeroDivisionError:
    print("Durch Null teilen nur Idioten")
#Wenn der User ein Buchstaben eingibt, erfolgt dieser Fehler:
except ValueError:
    print("Bitte gib eine Zahl ein!")
#Sollte kein Fehler auftreten, dann wird diese Ausgabe angezeigt.
else:
    print("Das Ergebnis ist:", ergebnis)
#Der User erhält diese Nachricht auf jeden Fall, egal was er eingibt.
finally:
    print("Das Programm wird nun beendet. Danke dass du da warst.")