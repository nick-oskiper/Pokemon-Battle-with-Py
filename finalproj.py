# Project: Pokemon game simulator

import random

print("""\nHello! Welcome to the Pokemon Game. Your objective in this game is to become powerful enough to beat
Pokemon trainers!
(Note: You will need to press 'Enter' to move through dialogue, and type numbers to do certain actions)
------------------------------------------
Your journey is about to begin. Have fun!! 
-----------------------------------------
""")


type_chart = {("Fire","Water"): 0.5, 
              ("Fire","Fire"): 1, 
              ("Fire","Grass"): 2,
              ("Water","Water"): 1,
              ("Water","Fire"): 2,
              ("Water","Grass"): 0.5,
              ("Grass","Water"): 2,
              ("Grass","Fire"): 0.5,
              ("Grass","Grass"): 1}

class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = self.level * 5
    
    @property
    def fainted(self):
        if self.health <= 0:
            return True
            
        else:
            return False
    
    def __str__(self):
        return f"{self.name}, level {self.level}"
    
    def hit(self,dmg):
        if not self.fainted:
            self.health -= dmg
            return f"{self.name} is now at {self.health} health"
        else:
            return f"{self.name} is already defeated"
    
    def attack(self, other):
        if isinstance (other,Pokemon):
            if not self.fainted:
                return other.hit(self.level * type_chart[(self.type, other.type)])
            else:
                return "Nooo, the Pokemon has fainted"

        

squirtle = Pokemon("Squirtle", 10,"Water")
charmander = Pokemon("Charmander", 10,"Fire")
bulbasaur = Pokemon("Bulbasuar", 10,"Grass")

# print(squirtle.attack(charmander))

wormadam = Pokemon("Wormadom", 10,"Grass")
scorbunny = Pokemon("Scorbunny", 10,"Fire")
buizel = Pokemon("Buizel", 10,"Water")

growlithe = Pokemon("Growlithe", 10,"Fire")
chimchar = Pokemon("Chimchar", 10,"Fire")
ponyta = Pokemon("Ponyta", 10,"Fire")
oshawatt = Pokemon("oshawatt", 10,"Water")
piplup = Pokemon("piplup", 10,"Water")
magikarp = Pokemon("magikarp", 10,"Water")
turtwig = Pokemon("Turtwig", 10,"Grass")
roselia = Pokemon("Roselia", 10,"Grass")
bonsly = Pokemon("Bonsly", 10,"Grass")


class Trainer:
    def __init__(self, name, level, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.is_first = True
        self.is_first2 = True
        self.is_first3 = True
        self.is_first4 = True
        self.name = name
        self.level = level

    def __str__(self):
        return f"Trainer {self.name} is level {self.level} and has Pokemon:\n{self.p1}\n{self.p2}\n{self.p3}"

    def vs(self, other):
        if isinstance(other, Trainer):
            print(f"{self.name} sent out {self.p1}\n{other.name} sent out {other.p1}")
            print(f"{self.name} attacked!")
            return Pokemon.attack(self.p1, other.p1)

    def vs2(self, other): # very complicated, inefficient definition 
        if isinstance(other, Trainer):
            if self.p1.health > 0 and other.p1.health > 0:
                print(f"{self.p1} attacked!")
                return Pokemon.attack(self.p1, other.p1)
            elif self.p1.health > 0 and other.p1.fainted and other.p2.health > 0:
                print(f"{self.p1} attacked")
                return Pokemon.attack(self.p1, other.p2)
            elif self.p1.health > 0 and other.p2.fainted and other.p3.health > 0:
                print(f"{self.p1} attacked")
                return Pokemon.attack(self.p1, other.p3)
            elif self.p2.health > 0 and type(other.p2) == Pokemon and other.p2.fainted and other.p3.health > 0:
                print(f"{self.p2} attacked")
                return Pokemon.attack(self.p2, other.p3)
            elif self.p1.fainted and self.p2.health > 0:
                if self.p1.fainted and self.is_first:
                    self.is_first = False
                    print(f"{self.name} lost one Pokemon")
                    print(f"{self.name} sent out {self.p2}")
                if other.p1.health > 0:
                    print(f"{self.p2} attacked")
                    return Pokemon.attack(self.p2, other.p1)
                elif other.p1.fainted:
                    if self.p2.fainted and self.is_first2:
                        self.is_first2 = False
                        print(f"{self.name} lost one Pokemon")
                        print(f"{self.name} sent out {self.p2}")
                    print(f"{self.p2} attacked")
                    return Pokemon.attack(self.p2, other.p2)
            elif self.p2.fainted and self.p3.health > 0:
                if self.p2.fainted and self.is_first3:
                    self.is_first3 = False
                    print(f"{self.name} lost one Pokemon")
                    print(f"{self.name} sent out {self.p3}")
                if type(other.p2) == Pokemon and other.p2.health > 0 and other.p1.fainted:
                    print(f"{self.p3} attacked")
                    return Pokemon.attack(self.p3, other.p2)
                elif type(other.p2) == Pokemon and other.p2.health > 0 and other.p1.health > 0 or type(other.p2) == str:
                    print(f"{self.p3} attacked")
                    return Pokemon.attack(self.p3, other.p1)
                elif type(other.p2) == Pokemon and other.p2.fainted:
                    if self.p3.fainted and self.is_first4:
                        self.is_first4 = False
                        print(f"{self.name} lost one Pokemon")
                        print(f"{self.name} sent out {self.p3}")
                    print(f"{self.p3} attacked")
                    return Pokemon.attack(self.p3, other.p3)



pip = Trainer("Schoolboy Pip", 10, growlithe, chimchar, ponyta)
maisie = Trainer("Surfer Maisie", 10, oshawatt, piplup, magikarp)
timmy = Trainer("Explorer Timmy", 10, turtwig, roselia, bonsly)
# user = Trainer("You", 10, buizel, scorbunny, wormadam)
# print(pip.vs(maisie))


def print_wait(in_str):
    print(in_str)
    input()

def num_wait(in_str):
    print(in_str)
    list_str = in_str.split()
    mydict = dict()
    mydict[int(list_str[4])] = list_str[5]
    mydict[int(list_str[6])] = list_str[7]
    mydict[int(list_str[8])] = list_str[9]
    cond = True
    while cond:
        user_input = input()
        if user_input == "1":
            print(f"You chose 1: {mydict.get(1)}")
            cond = False
            return mydict.get(1)
        elif user_input == "2":
            print(f"You chose 2: {mydict.get(2)}")
            cond = False
            return mydict.get(2)
        elif user_input == "3":
            print(f"You chose 3: {mydict.get(3)}")
            cond = False
            return mydict.get(3)
        else:
            print("Invalid option. Try again:")

def capture_beg(in_str):
    print(in_str)
    cond = True
    while cond:
        user_input = input()
        if user_input == "c":
            print("You captured the Pokemon:")
            cond = False
        else:
            print("Invalid option. Try again:")

def capture(in_str):
    count = 0
    print(in_str)
    user_input = input()
    if user_input.lower() == "c":
        print("You captured the Pokemon:")
        count +=1
        return count
    else:
        print("The Pokemon escaped")
        return count

def num_chance():
    captured = 0
    pokelist = []
    while True:
        input("You walk around.")
        rand_num = random.random()
        if rand_num < 0.2:
            print(wormadam)
            x = wormadam
            captured += capture("Press c to capture")
            print("Wormadam")
            if x not in pokelist:
                pokelist.append(x)
        elif 0.2 <= rand_num < 0.4:
            print(scorbunny)
            y = scorbunny
            captured += capture("Press c to capture")
            print("Scorbunny")
            if y not in pokelist:
                pokelist.append(y)
        elif 0.4 <= rand_num < 0.6:
            print(buizel)
            z = buizel
            captured += capture("Press c to capture")
            print("Buizel")
            if z not in pokelist:
                pokelist.append(z)
                
        if len(pokelist) == 3 and captured >= 3:
            break

        
def village_func():
    print_wait("You have entered the village!")
    print_wait("Ahead are three trainers! They won't let you in without a fight!")
    x = num_wait("Who will you fight? 1 Pip 2 Maisie 3 Timmy")
    if x == "Pip":
        attack_seq(pip,user)
    elif x == "Maisie":
        attack_seq(maisie,user)
    else:
        attack_seq(timmy,user)


def attack_seq(opp, you):
    print_wait(opp.vs(you))
    while True:
        print_wait(you.vs2(opp))
        if opp.p1.health <= 0 and opp.p2.health <= 0 and opp.p3.health <= 0:
            break
        print_wait(opp.vs2(you))
        if you.p1.health <= 0 and type(you.p2) == str:
            print("No more Pokemon, you lose. But you can always play again with a different strategy!")
            break
        if you.p1.health <= 0 and type(you.p2) == Pokemon and you.p2.health <= 0 and you.p3.health <= 0:
            break

    if opp.p1.health <= 0 and opp.p2.health <= 0 and opp.p3.health <= 0:
        print("---------------------------------------------------------------------------------------")
        print(f"Winner is {you.name}! You can either play the game again or leave! Thanks for playing!")
        print("---------------------------------------------------------------------------------------")
    elif you.p1.health <= 0 and type(you.p2) == Pokemon and you.p2.health <= 0 and type(you.p2) == Pokemon and you.p3.health <= 0:
        print("---------------------------------------------------------------------------------------")
        print(f"Winner is {opp.name}! You can either play the game again or leave! Thanks for playing!")
        print("---------------------------------------------------------------------------------------")

def forest_func():
    print_wait("You enter the Forest")
    print_wait("You don't see any Pokemon yet, but you can sense they are near.")
    print_wait("The professor said that there are three main Pokemon that live here, but they can be rare. You want to catch all three before leaving.")
    print_wait("You know that if you walk around you have a chance of finding Pokemon. (continue walking around until you capture all three)")
    num_chance()
    print("Congratulations! You've captured all three Pokemon.")



print_wait("You wake up on a sandy beach. The only thing you remember is your name (press 'Enter' to continue through dialogue).")
print_wait("You get up and see a man in the distance.")
print_wait("The man approaches you. He is wearing a white lab coat.")
print_wait("'Hello! Who are you? You fell from the sky from that rift up there!'")
print_wait("You look up and sure enough, there is a rift.")
print_wait("'I'm the Professor and I've just lost my Pokemon. Could you help me get them back?'")
print_wait("There are three Pokemon running away from him: Bulbasaur, Charmander, and Squirtle.")
print_wait("He hands you all his Pokeballs. 'The first one you catch, you can keep!'")
user_pok = num_wait("What will you do? 1 Bulbasaur 2 Charmander 3 Squirtle")
capture_beg("Type 'c' to capture")
print(user_pok,"!!")

if user_pok == squirtle.name:
    pok1 = squirtle
elif user_pok == charmander.name:
    pok1 = charmander
else:
    pok1 = bulbasaur

print_wait("You return the other two Pokemon to the Professor.")
user = Trainer("You", 10, pok1, "", "")
print_wait(f"Ah, so you've picked {user_pok}. Excellent choice.")
print("Well now you can either go to the Forest, which has wild pokemon you can catch,\
the village, which has trainers you can battle, or leave this world.")
choice1 = num_wait("What will you do? 1 Forest 2 Village 3 Quit ")
if choice1 == "Quit":
    print("You have quit the game. Thanks for Playing!")
elif choice1 == "Forest":
    print("You have entered the forest!")
    forest_func()
    user = Trainer("You", 10, buizel, scorbunny, wormadam)
    choice2 = num_wait ("What will you do? 1 Village 2 Quit 3 View-Pokemon")
    if choice2 == "Village":
        village_func()
    elif choice2 == "View-Pokemon":
        print_wait(f"After returning the {user_pok} to the Professor, your Pokemon team now consists of Buizel, Scorbunny, and Wormadam.")
        user = Trainer("You", 10, buizel, scorbunny, wormadam)
        print_wait(f"You decide to go to the village to test their might!")
        village_func()
    else: 
        print("Thank you for playing!")
else:
    village_func()
