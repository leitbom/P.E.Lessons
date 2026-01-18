## Faça um programa que leia três notas de um aluno, calcule sua média aritmética e imprima uma mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final.
## O critério de aprovação é o seguinte:
## ·aprovado (média >= 7);
## ·reprovado (média < 3);
## ·prova final ( 3 <= média < 7).

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

nota_final = (n1+n2+n3)/3

print(nota_final)

if nota_final >= 7:
    print("Aprovado!")

elif nota_final >= 3 and nota_final < 7:
    print("Prova final!")

else:
    print("Reprovado!")
