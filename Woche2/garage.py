#Liste der Autos in der Garage
autos = ["BMW", "Audi", "VW", "Fiat", "Seat", "Mercedes", "Porsche", "Trabbi", "Opel"]

print("Autos in der Garange: ")
for auto in autos:
    print(auto)

ausgeliehene_autos = input("Welche Autos sind derzeit ausgeliehen? (getrent durch Kommas) ")
ausgeliehene_autos = ausgeliehene_autos.split(",")

verbliebende_autos = [auto for auto in autos if auto not in ausgeliehene_autos]

print("Folgende Autos sind noch in der Garage:")
for auto in verbliebende_autos:
    print(auto)