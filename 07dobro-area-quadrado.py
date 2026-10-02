#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.#

medida = input('Informe o tipo da medida: ')

lado = float(input('Informe o tamanho de um lado do quadrado: '))

area = lado * lado

area_dobrada = area * 2

print('A área do quadrado é:', f"{area}{medida}", 'e o dobro da área é:', f"{area_dobrada}{medida}")