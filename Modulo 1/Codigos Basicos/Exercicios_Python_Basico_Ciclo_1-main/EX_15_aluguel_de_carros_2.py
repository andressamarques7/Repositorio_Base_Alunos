# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
# Sabendo que o carro custa R$ 90 por dia e R$ 0.35 por km rodado


print("------------- ALUGUEL DE CARRO -------------")
print("ONIX = R$60")
print("FOX = R$ 50")
print("CIVIC = R$ 90")
print("UNO = R$ 40")
print("NENHUMA DAS OPÇÕES = R$ 60")
onix = 60
fox = 50
civic = 90
uno = 40 
nenhuma_das_opcoes = 60
modelo = input("Me informe o modelo do carro alugado:")
dias = int(input("Me informe quantos dias o carro foi alugado:"))
km = float(input("Me informe quantos quilometros foi percorrido com o carro:"))

if modelo == "ONIX":
    diaria = 60
    dias * diaria 
    extra = 0.15 * km
    total = diaria + extra
    print(f"Você rodou {km} km por {dias} dias, então o preço a ser pago é {total}")

elif modelo == "FOX":
    diaria = 50 
    dias * diaria 
    extra = 0.15 * km 
    total = diaria + extra 
    print(f"Você rodou {km} km por {dias} dias, então o preço a ser pago é {total}")

elif modelo == "CIVIC":
    diaria = 90 
    dias * diaria 
    extra = 0.15 * km 
    total = diaria + extra 
    print(f"Você rodou {km} km por {dias} dias, então o preço a ser pago é {total}")

elif modelo == "UNO":
    diaria = 40 
    dias * diaria 
    extra = 0.15 * km 
    total = diaria + extra 
    print(f"Você rodou {km} km por {dias} dias, então o preço a ser pago é {total}")

else:
    diaria = 60 
    dias * diaria 
    extra = 0.15 * km 
    total = diaria + extra 
    print(f"Você rodou {km} km por {dias} dias, então o preço a ser pago é {total}")







