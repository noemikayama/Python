
num = int(input("\n Insert an integer number: "))
div5 = num % 5
div3 = num % 3
if (div5 == 0):
    if (div3 == 0):
        print("\n\n\t The number can be divided by 3 and 5 \n\n")
    else:
        print("\n\n\t The number can only be divided by 5 \n\n")
elif (div3 == 0):
    print("\n\n\t The number can only be divided by 3 \n\n")