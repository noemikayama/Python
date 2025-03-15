# Program that asks for a password and sees if it's right
# If not, ask for it again 3 times
# After 3 times, stop reading and show message that the card has been blocked

password = 12345678
tries = 3

for cont in range(3):
    type_pass = int(input("\n\n Type in your password: "))
    if (type_pass == password):
        print("\n\n Correct password! \n\n")
        break
    else:
        print("\n\n Wrong password \n\n")

if(type_pass != password):
    print("\n\n\t Card blocked \n\n")


    