import random

score = 0
for r in range(20):
    if r != 0 and r != 19:
        nogEens = input("Wilt u nog een ronde spelen? (Y/N)\n>").lower()
        if nogEens == "n":
            exit()
    print("\nRonde " + str(r+1))
    getal = random.randint(1,1000)
    for p in range(10):
        print("\nPoging " + str(p+1))
        gok = int(input("Wat denkt u dat het getal tussen de 1 en 1000 is? Of als u ermee wilt stoppen typ 0\n>"))
        if gok == 0:
            exit()
        print("U heeft {} geraden".format(gok))
        if gok == getal:
            print("U heeft het getal goed geraden! Uw score is nu {}".format(score))
            score += 1
            break

        if abs(gok - getal) <= 20:
            print("U bent heel warm")
        elif abs(gok - getal) <= 50:
            print("U bent warm")

        if gok > getal:
            print("Lager")
        if gok < getal:
            print("Hoger")

        if p == 9:
            print("U heeft het getal {} niet kunnen raden! U gaat nu naar de volgende ronde".format(getal))
    print("\nScore is ",score)