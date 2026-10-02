#Faça um programa que peça o raio de um círculo, calcule e mostre sua área:#

medida = input('Informe o tipo da medida: ')

raio = float(input('Qual é o raio do círculo? '))

area = 3.14 * (raio * raio)

print('A área do círculo é:', f"{area}{medida}")