# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("| ______________________________ |SISTEMA DE PROVAS| ______________________________ |")
nome = input("Digite seu nome:")
prova1 = float(input("Digite a nota da sua primeira prova:"))
prova2 = float(input("Digite a nota da sua segunda prova:"))
prova3 = float(input("Digite a nota da sua terceira prova:"))

# Formúla de soma
soma = prova1 + prova2 + prova3

# Formúla de média 
media = soma / 3

print("| ______________________________ |INFORMAÇÕES| ______________________________ |")

print(f"Nome do aluno:{nome}")
print(f"Nota da primeira prova:{prova1}")
print(f"Nota da segunda prova:{prova2}")
print(f"Nota da terceira prova:{prova3}")

print("| ______________________________ |MÉDIA| ______________________________ |")
print(f"Aluno:{nome}")
print(f"Média:{media}")



