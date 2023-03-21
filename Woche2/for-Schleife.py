"""
#Die for-Schleife wird verwendet, um über Elemente eines Objektes zu iterieren.
#Was ist eine Iteration?
#Eine Iteration ist ein Prozess, bei dem eine Aktion oder eine Gruppe von Aktionen wiederholt wird.
"""

#Syntax einer for-Schleife
students =  ["Max", "Julia", "Gina"] # Das ist eine Liste
"""
for student in students: #student ist eine temporäre Variable, die den Wert des I
    print(student) #Einrückung nach der Schleife sehr wichtig
#For-Schleife iteriert die Liste "students" und gibt für jedes Element in der Liste dessen Wert aus.

#Man kann auch einzelne Zeichen eines Strings ausgeben
for letter in "letters":
    print("Das Wort enthält den Buchstaben: " + letter)

for i in range(10):
    print(i)
"""

for _ in range(2): #wiederholt die innere Schleife zwei mal
    for student in students:
        print(student)

for _ in range(10):
    print(_ +1, "Hallo Welt")