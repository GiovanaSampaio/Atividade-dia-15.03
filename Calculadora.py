import math 

nome = input("digite seu nome: ")
print("Opção 1: soma ")
print("Opção 2: subtração ")
print("Opção 3: divisão ")
print("Opção 4: multiplicação ")
print("Opção 5: potenciação ")
opcao = int(input("digite a opção desejada: "))
if opcao == 1:
    numero1 = float(input("digite o primeiro número da soma: "))
    numero2 = float(input("digite o segundo número da soma:  "))
    soma = numero1 + numero2 
    print(soma)
elif opcao == 2:
    numero1 = float(input("digite o primeiro número da subtração: "))
    numero2 = float(input("digite o segundo número da subtração:  "))
    subtracao = numero1 - numero2
    print(subtracao)
elif opcao == 3:
    print("Lembrando que não pode dividir nenhum número por 0")
    numero1 = float(input("digite o primeiro número da divisão: "))
    numero2 = float(input("digite o segundo número da divisão:  "))
    divisao = numero1 / numero2 
    print(divisao)
elif opcao == 4:
    numero1 = float(input("digite o primeiro número da multiplicação: "))
    numero2 = float(input("digite o segundo número da multiplicação:  "))
    multiplicacao = numero1 * numero2
    print(multiplicacao)
elif opcao == 5:
    numero1 = float(input("digite o primeiro número da potenciação: "))
    numero2 = float(input("digite o segundo número da potenciação:  "))
    potenciacao = math.pow(numero1,numero2)
    print(potenciacao)
