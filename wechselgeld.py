print ("zu Zahlen 16.83€")
print ("gezahlt mit 50.00€")

zuZahlen = 16.83
gezahltMit = 50.00

Wechselgeld = gezahltMit - zuZahlen

print ()
print (f"Sie bekommen {Wechselgeld:.2f}€ zurück")
print ()

# E20 = int(Wechselgeld / 20)
E20 = Wechselgeld // 20
E10 = Wechselgeld // 10

print(f"{E20:.0f} * 20€")
print(f"{E10:.0f} * 10€")