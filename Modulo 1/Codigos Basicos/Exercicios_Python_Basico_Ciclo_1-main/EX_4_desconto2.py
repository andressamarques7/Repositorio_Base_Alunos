# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Seja bem-vindo(a), vamos iniciar a análise do desconto dos produtos")
nome = input("Informe o produto:")
preco = float(input(f"Informe o preço do {nome}:"))
porcentagem = float(input("Informe a porcentagem de desconto:"))

# Formúla do desconto
desconto = preco * (porcentagem / 100)

# Formúla do valor final
valor_final = preco - desconto

print(f"O {nome} com {desconto} de desconto custará {valor_final}")