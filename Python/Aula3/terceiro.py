#condições lógicas
#if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usado por múltiplas condições ).
# else: "Senão" (executa se nenhuma das anteriores forem verdadeira).

# print("Verificar maioridade")
# idade = int(input("Digite sua idade"))

# if idade > 18:
#     print("Você é adulto")
# elif idade >= 16:
#   print("Você não é adulto mais pode votar")
# else:
#    print("Você é adolescente")

#  #Sinais de > Maior e >= Maior Igual
#  #Sinais de < Menor e <= Menor Igual 
#  #Sinais de == Igual 

#  #Exemplo2 
# print("print loja")
# print("Bem-Vindo ao sistma da Dandara")
# print("Opções:")
# print("1 - Sapatos")
# print("2 - Roupas")
# print("3 - Perfumes")

# escolha = int(input("Digite sua escolha pelo número da opção:"))
# if escolha == 1:
#    print("Voce quer comprar sapatos, OK")
#    v1 = float(input("Digite o valor do produto:"))
#    qt1 = int(input("Digite a quantidade desejada:"))
#    total = v1 * qt1 
#    print("Sua compra de Sapatos foi um total de:",total)

# elif escolha == 2:
#    print("Você escolheu Roupas")
# elif escolha == 3: 
#    print("Você escolher Perfumes")
# else: 
#    print("Obrigada por utilizar o sistema da Dandara")  

# #Exemplo 3  
# print("Séries = S")
# print("Filmes = F")
# Categoria = input ("Digite sua categoria")
# if categoria == "S":
#    print("Voce escolheu por Séries")
# elif categoria == "F":
#    print ("Voce escolheu por filmes")
# else:
#    print("Voce não escolheu nenhuma das opções acima")
#    print("Estamos encerrando o aplicativo")

# #Exercício 1 
# #Crie um algoritimo que simule uma calculadora e que por opção de escolha permita calcular os operadores.
# # Ex: Ao escolher a opçaõ 1, ele irá calcula a soma e assim por diante.Sua calculadora deve conter todos os operadores

# print("Minha calculadora") 
# print("Operadores Matematicos") 
# print("Para Somar - Digite Som")
# print("Para subtrair - Digite Sub ")
# print("Para Multiplicar - Digite Mult")
# print("Para Dividir - Digite Div") 

# operadores = input("Digite sua escolha de operadores")

# if operadores == "Som":
#    soma1 = float(input("Digite o primeiro valor"))
#    soma2 = float(input("Digite o segundo valor"))
#    tsoma = soma1 + soma2 
#    print("O calculo de soma foi:",tsoma)
# elif operadores == "Sub":
#    sub1= float(input("Digite o primeiro valor"))
#    sub2= float(input("Digite o segundo valor"))
#    tsub = sub1 + sub2 
#    print("O calculo de subtração foi:",tsub)

   #Exercício 2 

# print("Digite para prosseguir com as perguntas")
# nome= (input("qual é seu nome?"))
# curso = (input("qual é seu curso?"))
# anoatual = float(input("Digite o ano atual"))
# Idade = float(input("Informe seu ano de nascimento para saber sua idade"))

# total=anoatual-Idade
# print("Seu nome é: ", nome, "Seu curso foi:", curso, "E sua idade é :", total)