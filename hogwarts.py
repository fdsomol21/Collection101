#francis
#hogwarts.py
#randomly assign a house to a person
import random
import time
def house(name):
    name = name.capitalize()
    if name == "harry" or name == "Ron" or name =="Hermione":
        return "Gryffindor"
    elif name == "Newt" or name == "Nymphadora" or name == "Pomona":
        return "Hufflepuff"
    elif name == "Luna" or name == "Cho" or name == "Filius":
        return "Ravenclaw"
    elif name == "Voldemort" or name == "Draco" or name == "Severus":
        return "Slytherin"
    else:
        return random.choice(["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])
def main():
    print("Welcome to Hogwarts!")
    user_name = input("Enter your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("....")
    assigned_house = house(user_name)
    print(f"{user_name}, you have been assigned to {assigned_house}!")
main()

