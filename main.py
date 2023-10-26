
def middel_getal():
    while True:
        getal1 = int(input("Vul hier het 1ste getal in: "))
        getal2 = int(input("Vul hier het 2de getal in: "))
        getal3 = int(input("Vul hier het 3de getal in: "))

        if getal1 <= getal2 <= getal3 or getal3 <= getal2 <= getal1:
            middelste_getal=getal2
            print(middelste_getal)

        elif getal2 <= getal1 <= getal3 or getal3 <= getal1 <= getal2:
            middelste_getal=getal1
            print(middelste_getal)

        else:
            middelste_getal=getal3
            print(middelste_getal)


middel_getal()