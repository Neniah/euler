print("""Entras en una habitación oscura donde hay dos puertas.
¿Cuál eliges? La puerta #1 o la puerta #2?
""")

door = input("> ")

if door == "1":
    print("Hay un gran oso comiendose una tarta de queso.")
    print("¿Qué vas a hacer?")
    print("1. Coger el pastel.")
    print("2. Gritar al oso.")

    bear = input("> ")

    if bear == "1":
        print("The bear eays your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retire.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of...")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good bye!")
