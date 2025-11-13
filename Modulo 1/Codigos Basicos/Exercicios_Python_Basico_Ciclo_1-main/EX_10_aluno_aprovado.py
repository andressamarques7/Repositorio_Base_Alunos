# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("| ______________________________ |SISTEMA DE PROVAS| ______________________________ |")

prova1 = float(input("Digite a nota da sua primeira prova:"))
prova2 = float(input("Digite a nota da sua segunda prova:"))
media = (prova1 + prova2) /2
aprovado = (media >7) and prova1 >0 and prova2 >0
print(f"Você foi aprovado? {aprovado}")