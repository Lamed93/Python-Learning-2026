'''
Faça um programa que peça 2 números inteiros e um número real.
Calcule e mostre: O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''

inteiro_1 = int(input("Digite o primeiro número inteiro: "))
inteiro_2 = int(input("Digite o segundo número inteiro: "))
real_1 = float(input("Agora digite um número real: "))

calc_1 = (inteiro_1 * 2) * (inteiro_2 / 2)
calc_2 = (inteiro_1 * 3) + (real_1)
calc_3 = real_1 ** 3

print(f"1º Cálculo: O produto do dobro primeiro com metade do segundo: {calc_1:.2f}")
print(f"2º Cálculo: A soma do triplo do primeiro com o terceiro: {calc_2:.2f}")
print(f"3º Cálculo: O terceiro elevado ao cubo: {calc_3:.2f}")