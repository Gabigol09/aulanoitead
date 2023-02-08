nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

media_aproveitamento = (nota1 + nota2*2 + nota3*3 + media_exercicios)/7

if media_aproveitamento >= 9:
    conceito = "Aprovado"
elif media_aproveitamento <= 4:
    conceito = "Reprovado"
else:
    conceito = "E"

print("A média de aproveitamento é:", media_aproveitamento)
print("O conceito do aluno é:", conceito)
