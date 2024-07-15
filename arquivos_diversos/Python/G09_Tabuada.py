cont = 1
num = int(input("Digite um numero para ver sua tabuada: "))
while cont < 11:
    result = num * cont
    print("{} x {} = {}".format(num, cont, result))
    cont = cont + 1