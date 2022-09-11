'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0          A
    Entre 7.5 e 9.0           B
    Entre 6.0 e 7.5           C
    Entre 4.0 e 6.0           D
    Entre 4.0 e zero          E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.
'''

from tkinter import E


nota1 = input('Digite o valor da primeira nota: ')
nota2 = input('Digite o valor da segunda nota: ')

media = (float(nota1)+float(nota2))/2

if(float(media) <= 4):
    conceito = 'E'

elif(4 < float(media) <= 6):
    conceito = 'D'

elif(6 < float(media) <= 7.5):
    conceito = 'C'

elif(7.5 < float(media) <= 9):
    conceito = 'B'

elif(9 < float(media) <= 10):
    conceito = 'A'

print('Primeira nota:\t', nota1)
print('Segunda nota:\t', nota2)
print('Media:\t\t', media)
print('Conceito:\t', conceito)

if(float(media) <= 6):
    print('REPROVADO')

elif(float(media) > 6):
    print('APROVADO')