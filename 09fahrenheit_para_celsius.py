#Faça um programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

fah = float(input('Digite a temperatura em fahrenheit: '))

fah_para_cel = (fah - 32) * 5/9

print('O resultado da conversão de fahrenheit para celsius é:', f"{fah_para_cel:.2f}C°")