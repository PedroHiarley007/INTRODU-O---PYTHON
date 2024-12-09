#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

#Peso estabelecido que não pode exceder é 50kg
# multa 4,00 reais por kilo excedente 

#inserir o peso
peso = float(input("Quantos kilos de peixe?:"))

#valor limite sem multa
peso_limite = 50

#Se o peso for mais alto que o limite
if peso > peso_limite:
    peso_excedente = peso - 50
    print(f"Você excedeu {peso_excedente}kg")
    multa = peso_excedente * 4.00
    print(f"Você pagará {multa} de multa")

if peso <= peso_limite:
    print(f'Você não excedeu o limite de peso :D')
