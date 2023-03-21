#msh

while True:
    eingabe = input("$>> ")
    x = eingabe.split(" ")
    if x[0] == "echo":
        for i in range(1, len(x)):
            print(x[i], end=" ")
        print ()
    elif x[0] == "exit":
        break
    elif x[0] == "touch":
        if len(x) >= 2:
            for i in range(1, len(x)):
                open(x[i], "x")
        else:
            print("Bitte gib einen Dateinamen an.")