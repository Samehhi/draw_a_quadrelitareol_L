


def draw(x, y):
    for i in range(y):
        letter = "#" * x
        print(letter)
        


try:
    letter = input("Give the fucking retard cyka blayet letter that u want me you human : ")
    if letter.__len__() > 1:
        raise Exception("SORRY LITTLE SHIT, U PUT MORE THAT ONE LETTER GET FUCKED BY THE SYSTEM L BOZO")
    
    x = (int(input("Hello ! Give me the X coordinates : ")))
    y = (int(input("Hello ! Give me the Y coordinates : ")))

    

except TypeError:
    print("Error 101, The type that has been given is incorect or not readable please re try.")
except NotImplementedError:
    print("AYO AYO THE SHIP IS SINKING THIS IS BIG STUFF WE'RE FUCKED RESTART UR FKIN COMPUTER I DON'T WANNA DIE AAAAAAAAAAAAAAAAH !!!!!!")

print("Wow :")

print(draw(x, y))