# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


print("-------------- CALCULADORA -----------------")

pergunta1 = float(input("Me informe um número:"))
pergunta2 = float(input("Me informe outro número:"))

print("SOMA")
print("SUBTRAÇÃO")
print("MULTIPLICAÇÃO")
print("DIVISÃO")
opcao = input("Escolha uma opção:")
soma = pergunta1 + pergunta2
subtracao = pergunta1 - pergunta2
multiplicacao = pergunta1 * pergunta2
divisao = pergunta1 / pergunta1

if opcao == "SOMA":
    print(f"{pergunta1} + {pergunta2} = {soma}")
elif opcao == "SUBTRAÇÃO":
    print(f"{pergunta1} - {pergunta2} = {subtracao}")
elif opcao == "MULTIPLICAÇÃO":
    print(f"{pergunta1} * {pergunta2} = {multiplicacao}")
elif opcao == "DIVISÃO": 
    print(f"{pergunta1} / {pergunta2} = {divisao}")
else:
    print("Opção Inválida")