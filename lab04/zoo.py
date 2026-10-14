def show_help():
    print("Type 'help' to get a list of all the things you can do")
    print("Type 'see' to get a list of all the animals")
    print("Type 'pet' followed by the animal's name to pet a particular animal")
    print("Type 'bye' to leave the zoo and exit the program")


def show_all_animals():
    print("The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Marcus the Monkey 🐒")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")

def hug_animal(animal):
    if animal == "Clover":
        print("clover hops away")
    if animal == "marcus":
        print("Marcus hugs you back!")
    if animal == "coco":
        print("Coco baaaas")
    if animal == "arno":
        print("Arno eats you! 🐊")

def pet_animal(animal):
    if animal == "Clover":
        print("clover is so happy! ❤️")
    if animal == "marcus":
        print("Marcus waves hi!")   
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    else:
        print("Sorry, I don't know that animal")


print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do")
print()

while True:
    response = input("What would you like to do? ").strip().lower()
    if response == "help":
        show_help()
    elif response == "see":
        show_all_animals()
    elif response.startswith("hug"):
        animal = response[4:].strip()
        hug_animal(animal)
    elif response.startswith("pet"):
        animal = response[4:].strip()
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        break
    else:
        print("Sorry, I don't understand that command.")