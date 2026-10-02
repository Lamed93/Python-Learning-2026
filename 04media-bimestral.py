#Faça um programa que peça as 4 notas bimestrais e mostre a média.#

nota1 = float(input('Primeira nota bimestral: '))
nota2 = float(input('Segunda nota bimestral:  '))
nota3 = float(input('Terceira nota bimestral: '))
nota4 = float(input('Quarta nota bimestral:   '))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

print('A média das quatro notas bimestrais é:', media)