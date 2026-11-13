'''
Faça um programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.
Formula
F = (C * 9/5) + 32
'''

celsius = float (input(("Digite a temperatura em Celsius: ")))

celc_para_fahr = (celsius * 9/5) + 32

print(f"A temperatura C° {celsius:.1f}, convertida para F°, é: {celc_para_fahr:.1f}")