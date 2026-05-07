#1. O laço 'for' (Repetições Determinadas)
#Use o ' for' quando voce sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
#Exemplo: Relaório de produção diária
#Imagine que voce tem uma meta de produzir 5 lotes e quer numerar cada um:

#Exemplo 1 
# for lote in range(1, 6):
#    print(f"Processando lote número{lote},...")
#    print("Qualidade verificada.{ok}")
#    print("Produçãoo do dia finalizada!")

# #Imagina que voce queira atingir uma meta de produção de 5 carros e numera-los
# for carros in range(1,6): 
#   print(f"Produção de carros diaria {carros},...")

# # # Exemplo 2 
# # Contar até 4 
# for i in range(5):
#    print(i)

# # # Exemplo 3
# peças =["Engrenagem", "Eixo","Rolamento","parafuso","Martelo"]
# tipospeças = ["Barra Dentada","Porca Eixo","Anel externo","Parafuso Phillips","Martelo cabeça chata"]

# for item in peças + tipospeças:
#    print(f"Item de Estoque: {item} + {tipospeças}")
#    for tipos in tipospeças:
#       print(f"Minha lista de tipos de peças {tipospeças}")

# #Exemplo 4 
# #Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção voce deseja e a partir da seleção ele listar os produtos
# print("Loja de peças da Dandara")
# print("Bem Vindo")
# print("Escolha uma das opções")
# print("1-Peças")
# print("2- Tipos de peças")

# opção= int(input("Digite sua opção de pesquisa:"))

# # # Exercício 1 
# # # 1. Contador de Produção (for)
# # # Uma esteira processa 10 peças por ciclo.Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima:"Peça n° X processada com sucesso". No final, exiba "Ciclo de produção concluído"
# # (Variable) Ciclo:int 
# for ciclo in range(1, 11):
#    print(f"Peça n° {ciclo}processando com sucesso...")
# print("Ciclo de produção concluido...")

#Exercício 2
#Imagine a produção de frutas em uma feira.Desejo apresentar as frutas banana,manga,melancia,abacaxi.Com uma quantidade de 10 bananas , 5 mangas, 10 melancias e 13 abacaxi

# banana= ("banana")
# manga= ("manga")
# melancia= ("melancia")
# abacaxi=("abacaxi")

# for banana in range(1,11):
#    print(f"produção de frutas {banana}")
# for manga in range(1,6):
#    print(f"produção de frutas {manga}")
# for melancia in range(1,11):
#    print(f"produção de frutas {melancia}")
# for abacaxi in range(1,14):
#    print(f"produção de frutas {abacaxi}")
   
# #Exercício 3 
# #Montar uma tabuada inicialmente pode ser usado para um valor fixo e depois usar a pergunta 

# numero= int(input("Digite o valor"))
# print(f"Tabuada do {numero}")

# 2. O laço while (Repetições Indeterminadas)
#Use o while quando voce não sabe quando vai parar.Ele  depende de uma condição(como um sensor de segurança ou um botão de emergencia)

#Repete enquanto a temperatura(loop infinito controlado)

# Repete enquanto a temperatura estiver segura 
#início 

# Temperatura = 25
# while Temperatura < 40: 
#    print (f"Temperatura atual: {Temperatura}°C Sistema operando...")

#Exemplo: Menu de Interação 
#! = diferente 
#Lower minisculo 
#upper maiusculo 
opção = ""

while opção !="Sair" and "SAIR": 
   opção = input("Digite a leitura do sensor ou 'sair' para fechar:").lower().upper()
   if opção!= "Sair"and "SAIR":
      print (f"Dado '{opção}' registrado no banco de dados.")
print("Sistema encerrado.")

#and e or 
#and comparações verdadeiras e iguais 
#or comparações verdadeiras e não iguais 

#Exercício 4 
# Monitor de Pressão Crítica(While)
# Crie um simulador onde o usuário deve digitar compressor
# Enquanto a pressão for menor que 100 PS, o programa continua pedindo a nova leitura
# Assim que o usuario digitar um valor maior ou igual  a 100, o looop para e exibe a mensagem:"ALERTA: Pressão crítica atingida! Desligando o Sistema "

import time 
pressão = int(input("Digite o valor da pressão"))
while pressão <= 100:
  print (f"PSI atual:{pressão}°C. Gerando nova leitura...")
  time.sleep(2)
print("ALERTA! Temperatura atingiu o limite.Desligando motor...")

#Exercício 5 
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras tres.
#qualquer opção diferente sair do menu 



