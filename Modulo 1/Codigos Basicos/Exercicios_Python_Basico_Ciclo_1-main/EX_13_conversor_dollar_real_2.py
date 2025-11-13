# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("------------ CONVERSOR DE DOLLAR ---------------")
print("1 - Dollar para Real")
print("2 - Real para dollar")
opcao = int(input("Digite a opção:"))
            
if opcao ==1:
   cotacao1 = float(input("Digite a cotação do dollar:"))
   valor_em_dollar = float(input("Digite o valor em dollar a ser convetido para real:"))
   formula = cotacao1 * valor_em_dollar
   print(f"O valor em reais é: {formula}")

elif opcao ==2:
    cotacao2 = float(input("Informe a cotação atual do Dollar:"))
    quantidade_de_reais = float(input("Informe a quantidade de reais:"))
    formula2 = cotacao2 * quantidade_de_reais
    print(f"O valor em dólares é:{formula2}")



