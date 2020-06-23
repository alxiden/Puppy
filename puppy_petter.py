from random import choice

num_pets = 0
names = ["Spot","Fluffles","Rex"]
name = choice(names)

print("Meet {} hes a good boy and needs pets".format(name))


def Doggy():

    print("""           _        _       """)
    print("""          /\\      ,'/|      """)
    print("""        _|  |\-'-'_/_/      """)
    print("""   __--'/`           \      """)
    print("""       /              \     """)
    print("""      /        "o.  |o"|    """)
    print("""      |              \/     """)
    print("""       \_          ___\     """)
    print("""         `--._`.   \;//     """)
    print("""              ;-.___,'      """)
    print("""             /              """)
    print("""           ,'               """)
    print("""        _-'                 """)






def pet():
    global num_pets
    if action =="y":
        num_pets = num_pets + 1

    else:
        print("why would you not want to pet {}?".format(name))

def end():
    if num_pets == 10:
        print("{} was such a good boy he has accended to doggy Godhood, to say thank you hes granted you 1 of 3 wishes".format(name))
        print("1: Unlimited money!")
        print("2: True power")
        print("3: Pet {} one more time".format(name))
        answer = int(input("Which one do you choose?: "))
        if answer == 3:
            print("Well done! that was the correct answer, you shall now join me as my personal petter")
        elif answer == 2:
            print("Wrong!! you shall gain power but be forever hunted by those who seek to take it")
        elif answer == 1:
            print("Wrong!! you shall gain all the money you could evver want but you will be forever hunted by those who seek to take it")
        else:
            print("That wasnt one of the options, I'm surprised by how stuipid you are")




        

while True:
    Doggy()
    if num_pets == 0:
       action = input("Would you like to pet {} the puppy? (y/n): ".format(name)).strip().lower()
    else:
        action = input("Would you like to pet {} again? (y/n): ".format(name)).strip().lower()
    pet()
    print(num_pets)
    end()
    if action == "q" or num_pets >= 10:
        break
