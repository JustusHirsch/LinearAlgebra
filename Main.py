
m=float(input("gib die Steigung in Form von einer Zahl an. "))
b=float(input("gib den y-Achsenabschnitt in Form von einer Zahl an."))
Auswahl_xy=input("möchtest du x oder y ausrechnen?(x oder y) ")
# x=float(input("gib einen x-Wert "))
# x = x+1
# print("folgender x-Wert wurde gewählt",x)
if Auswahl_xy=="x":
    y=float(input("gib den y-Wert an. "))
    print("x=",(y-b) / m)
if Auswahl_xy=="y":
    x=float(input("gib den x-Wert an. "))
    print("y=",m*x + b)
