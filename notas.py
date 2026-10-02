nome = input("Digite o nome do aluno: ")
nota = float(input(f"Digite a nota de {nome}: "))
tem_nota = input(f"{nome} tem mais notas? ")


contador = 1


while tem_nota == "sim":
    notaS = input(f"Digite a nova nota de {nome}: ")

contador = contador + 1
media = (nota + notaS / contador )
print(f"Aluno: {nome}")
print(f"Média: {media}")

if media <= 7:
    print("Está aprovado!")
elif media <= 5:
    print("Quase! está de recuperação.")
else:
    print("Está reprovado.")
