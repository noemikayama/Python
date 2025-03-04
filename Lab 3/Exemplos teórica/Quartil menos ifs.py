num = int(input("\n Digite um número inteiro: "))
if (num >= 100) and (num < 1000):
    if (num <= 250):
        print("\n\t O número está no 1º Quartil \n\n")
    else:
        if (num <= 500):
            print("\n\t O número está no 2º Quartil \n\n")
        else:
            if (num <= 750):
                print("\n\t O número está no 3º Quartil \n\n")
            else:
                if (num <= 1000):
                    print("\n\t O número está no 4º Quartil \n\n")
else: 
    print("\n\t Fora do escopo \n\n")


