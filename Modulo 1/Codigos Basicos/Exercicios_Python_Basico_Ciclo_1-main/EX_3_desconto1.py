# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Seja bem-vindo(a), vamos iniciar a análise do desconto dos produtos")
      
      
preco = float(input("Qual o preço do produto?"))
porcentagem = float(input("Qual a porcentagem de desconto?"))

#Formúla de desconto 
desconto = preco * (porcentagem / 100)

print(f"Olá consultor_da_sephora, o produto que custa {preco} terá {porcentagem} de desconto.")