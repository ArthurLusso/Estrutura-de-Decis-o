# Crie um algoritimo que leia 3 valores referente (lados de um triângulo)
# Determine se formam um trinângulo, e se formar verifique
# se é um equilátero, isóceles ou escaleno

lado1 = float(input("Digite o valor do primeiro lado:"))
lado2 = float(input("Digite o valor do segundo lado:"))
lado3 = float(input("Digite o valor do terceirolado:"))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

    if (lado1 == lado2) and (lado2 == lado3):
        print ("Esse triângulo é equilátero")

    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print ("Esse trinângulo é isóceles")

    else:
        print("Esse triângulo é escaleno")

else:
    print("Isso não é um trinângulo")

