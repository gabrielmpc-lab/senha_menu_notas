def somar():
    numa1 = float(input("Digite o primeiro número: "))
    numa2 = float(input("Digite o segundo número: "))
    resultado = (numa1 + numa2)
    print(f"Resultado: {resultado}")

def subtrair():
    numb1 = int(input("Digite o primeiro número: "))
    numb2 = int(input("Digite o segundo número: "))
    resultadob = (numb1 - numb2)
    print(f"Resultado: {resultadob}")

def multiplicar():
    numm1 = int(input("Digite o primeiro número: "))
    numm2 = int(input("Digite o segundo número: "))
    resultadom = (numm1 * numm2)
    print(f"Resultado: {resultadom}")

def dividir():
    numd1 = int(input("Digite o primeiro número: "))
    numd2 = int(input("Digite o segundo número: "))
    resultadod = (numd1 / numd2)
    print(f"Resultado: {resultadod}")

def pares():
    quantidade = int(input("digite quantos dos números pares você quer: "))
    contador = 0
    numero = 1
    while contador < quantidade:
        if numero % 2 == 0:
            print(f"Eis os números: {numero}")
            contador += 1
        numero += 1

def impares():
    quantidade = int(input("Digite quantos dos números ímpares você quer: "))
    contador = 0
    numero = 0
    while contador < quantidade:
        if numero % 2 != 0:
            print(f"Eis os números: {numero}")
            contador += 1
        numero += 1

def somatorio():
    quantidade = int(input("digite quantos dos números pares você quer: "))
    contador = 0
    numero = 1
    while contador < quantidade:
        if numero % 2 == 0:
            print(f"Eis os números: {numero}")
            contador += 1
        numero += 1

def sair():
    print("Saindo do sistema...")

while True:

    print("CALCULADORA")
    print("1 - adição")
    print("2 - subtracão")
    print("3 - multiplicacão")
    print("4 - divisão")
    print("5 - pares")
    print("6 - ímpares")
    print("7 - somatório")
    print("8 - fatorial")
    print("0 - sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        somar()

    elif opcao == "2":
        subtrair()

    elif opcao == "3":
        multiplicar()
        
    elif opcao == "4":
        dividir()

    elif opcao == "5":
        pares()
    
    elif opcao == "6":
        impares()

    elif opcao == "7":
        somatorio()

    elif opcao == "0":
        sair()
        break

    else:
        print("Opção inválida, tente novamente!")