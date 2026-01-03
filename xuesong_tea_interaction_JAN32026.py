# Testing console based chapter of Vaelren's Character, Xuesong :D
# what i'm testing exactly: conditional logic, input handling, state tracking
# works on windows only

friendliness = 0
professionalism = 0
negativity = 0
#stats above
YN=input("What is your name? ")
#asks for the user's name
print( )
def introduction():
    print("You are a servant for Xuesong Shan, the Excellency of Vaelren")
print( )
input("Press Enter to continue...")
print( )
print("Xuesong: Greetings,",YN,". How are you faring today?")
input("Press Enter to continue...")
print( )
#choice here
print("It seems like the Excellency is asking about your day. Do you")
print("A: Tell him about your day (+5 friendliness)")
print("B: Tell him to not worry about such trifling matters (+5 professionalism)")
print( )
#I plan to make it so that, this stats influence endings
print( )
#user picks A or B or something else
while True:
    choices = input("What do you do? (A/B): ").strip().upper()
    if choices == "A":
        friendliness += 5
        print("You tell him about your day, he smiles and nods and pours your tea.")
        break
    elif choices == "B":
        professionalism += 5
        print("You tell him not to worry about you, his face turned solemn and he waits for you to pour his tea.")
        break
    elif choices == "Spill the tea":
        negativity += 10
        print("You decide to spill tea on him, he gets mad at you but shrugs it off.")
        print("Your negativity is:", negativity)
        break
    else:
        print("Invalid choice! The Excellency looks at you, confused, he shrugs it off.")
        break

# the C path is a secret path for fun haha

print( )
input("Press Enter to continue...")
print("Stats after your choice")
print("Friendliness:", friendliness)
print("Professionalism:", professionalism)
print("Negativity:", negativity)

#Thank you for interacting with this story!