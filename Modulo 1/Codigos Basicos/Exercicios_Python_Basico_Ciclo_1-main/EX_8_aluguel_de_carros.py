# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("------------------------------------------ ALUGUEL DE CARRO -----------------------------------------------------------")
km_rodado = float(input("Informe a quantidade de km percorrido:"))
dias = int(input("Informe quantos dias ele foi alugado:"))
diaria = 60
km = 0.15

# Formúla da diaria 
formula1 = diaria * dias 

# Formúla do km 
formula2 = km_rodado * km 

# Formúla do valor
formula3 = formula1 + formula2 

print(f"Você andou {km_rodado} por {dias} dias, então o preço a pagar é: R${formula3}")