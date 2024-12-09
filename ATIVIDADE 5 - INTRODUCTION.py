# *DESAFIO* 
#Verificador de idade se for maior de idade, mostre na tela Você é maior de idade, se for menos de idade Voce é menor de idade e se tiver mais que 64 anos, mostre você é idoso

#identificador_de_idade

# O usuário vai inserir a idade

idade = int(input("Qual a sua idade?:"))

# Se a idade for menor que 18, o usuário é menor de idade

if idade < 18:
    print("Você é menor de idade")

#Se a idade for maior ou igual a 18, o usuário é maior de idade

if idade >= 18 and idade < 64:
    print("Você é adulto")

# Se a idade for maior ou igual a 64, o usuário é idoso

if idade >= 64:
    print("Você é idoso")



