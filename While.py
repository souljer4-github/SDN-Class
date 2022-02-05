game = input("Would you like to play a game? ")
game = game.lower()
if game == "no":
    print("Thanks for playing!")
else:
    while game == "yes" or "y":
        color = input("What is your favorite color? ")
        age = int(input("How old are you? "))
        name = input("What is your name? ")
        pd1 = {"Name": [], "age": [], "Color": []}
        pd1["Name"].append(name)
        pd1["age"].append(age)
        pd1["Color"].append(color)
        print(pd1)
        check = str(input("Do you want to start over?"))
        check = check.lower()
        if check == "yes" or "y":
            continue
        if check == "no" or "n":
            break
        print("Thanks for playing!")
