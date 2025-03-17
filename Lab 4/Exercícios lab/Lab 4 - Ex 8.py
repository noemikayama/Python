N = int(input("\n\n Insert how many numbers of the sequence: "))
 
num1 = 2
num2 = 3

if N==1:
    S=2
    print(num1)
elif(N==2):
    S=5
    print(num2)
else:
    print("\n\n")
    S=5
    print(f"{num1} + {num2}", end=" ")
    for count in range(2, N):

        aux = num2
        num2 = num1 + aux
        num1 = aux
        print(f"+ {num2}", end= " ")
        S+=num2
    
print(f" = {S} \n\n")