#Syntax der While-Schleife
#while Bedungung

count = 1

while count <= 10:
    print(count)
    count += 1 #erhöht count um 1 nach jeder Iteration

i = 1
n = 5

while i <= n:
    print (n)
    n = n - 1

#______________________________________________________

# Die Schleife wird so lange ausgeführt, solang der Benutzer nicht Ende eingibt.

while True:
    user_input = input("Geben Sie etwas ein (oder 'ende', um das Programm zu beenden): ")

    if user_input == 'ende':
        break #Beendet die Schleife wenn der Benutzer "Ende" eingibt.

    print ("Sie haben ",user_input, " eingegeben.")