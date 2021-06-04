#    Validador de CPF com a função de verificar se um CPF é ou não válido
cpf_dig = input("digite o cpf: ")
tam_cpf_01 = len(cpf_dig)
lista_cpf = []
multiplicador = 10    # multiplicara o penultimo numero do cpf
multiplicador2 = 11   # multiplicara o ultimo numero do cpf
novo_num = 0
novo_num2 = 0
soma_total = 0
soma_total2 = 0

contador = 0   

for n in cpf_dig:
    n = int(n)

    if contador < 9:
        novo_num = multiplicador * n           # numero ao ser multiplicado correspondente ao penultimo numero
        soma_total = soma_total + novo_num  # serve para acumular o novo num apos multiplicar e será usado no calculo
        if multiplicador > 2:
            multiplicador -= 1   #decresce uma unidade do multiplicador pois no produto ele vai decrescendo

        else:
            print("")
    else:
        print("")

    if contador < 10:
        novo_num2 = multiplicador2 * n    # numero ao ser multiplicado correspondente ao ultimo numero

        soma_total2 = soma_total2+novo_num2  # serve para acumular o novo num apos multiplicar e será usado no calculo

        if multiplicador2 > 1:
            multiplicador2 -= 1

        else:
            multiplicador2 = 0
    else:
        continue
    contador += 1


penultimo = 11 - (soma_total % 11)  # formula que o luiz otavio informou no case, serve para o penultimo
ultimo = 11 - (soma_total2 % 11)     # formula que o luiz otavio informou no case, serve para o penultimo

if penultimo > 9:
    penultimo = 0
else:
    print()

if ultimo > 9:
    ultimo = 0
else:
    print()

print(penultimo)
print(ultimo)
lista_cpf.append(penultimo)
lista_cpf.append(ultimo)

check1 = 0
check2 = 0
cont = 0
for num in cpf_dig:
    cont += 1
    if cont == 10:
        if int(num) == penultimo:
            check1 = 1
        else:
            print()
    if cont == 11:
        if int(num) == ultimo:
            check2 = 1
        else:
            print("")
    else:
        continue

if check1 == 1 and check2 == 1:
    print(" CPF VÁLIDO ")
else:
    print("CPF INVALIDO")
