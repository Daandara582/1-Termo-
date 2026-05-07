#Exercício1 
# print("Registros de veículo")
# modelo_veiculo=input("Informe é o modelo do veículo?")
# placa_veiculo=input("Informe é a placa do veículo?")
# print(f"Veiculo{modelo_veiculo} de placa{placa_veiculo}registrado no sistema. Boa Viagem!")

# #Exercício2
# print("Calculo de autonomia")
# capacidade_tanque = float(input("Digite a capacidade dp tanque de litros "))
# consumo_médio= float(input("Digite o consumo do caminhão em km/1"))
# distancia_total = capacidade_tanque * consumo_médio 
# print(f"Capacidade {capacidade_tanque} do tanque a sua distancia {distancia_total}")

#Exercício3
# print("Conversor de moeda(Frete internacional)")
# valor_frete=float(input("Valor de frete em Dólar"))
# conversao_real=float(input("Valor da taxa em reais"))
# total_conversão=valor_frete * conversao_real 
# print(f"O valor do frete foi{valor_frete} e a taxa aplicada foi de {conversao_real}e o total do frete {total_conversão:.2f}")
# print("O valor do frete foi ",valor_frete,"E a taxa aplicada foi de",conversao_real,"E o total do frete",round(total_conversão,2))

# #Exercício4
# print("Média de Entregas")
# rota1=int(input("Digite a primeira rota em horas"))
# rota2=int(input("Digite a segunda rota em horas"))
# rota3=int(input("Digite a terceira rota em horas"))
# media_rota=(rota1+rota2+rota3)/2 
# print(f"A média de entregas das rotas realizadas foi de...{media_rota:.2f}")

#Exercício5
# print("Monitor de carga ")
# Peso_caminhão=float(input(" Informe o peso do caminhão em toneladas"))
# if Peso_caminhão <= 10: 
#     print("Carga Leve ")
# elif Peso_caminhão <=25:
#     print("Carga padrão")
# else:
#     print("ALERTA: excesso de peso")

#Exercício6 
# print("Classificador de Destinos")
# print("Codigos de cargas=N -Norte S - Sul e outros internacional ")
# codigo_carga=input("Inserir o codigo da carga") 
# if codigo_carga == "N":
#     print("Região Norte")
# elif codigo_carga == "S":
#     print("Região Sul")

# else:
#     print("Região internacional")
   # lower() #Texto minusculo 

#Exercício7
# print("Liberação de Saída- Checklist e motorista")
# checklist=input("O checklist foi realizado (Concluido ou Não concluido)")
# motorista=input("O motorista foi identificado(Sim ou Não)")
# if checklist == "Concluido" and  motorista == "Sim":
#     print("Iniciar Rota- Boa Viagem ")
# else:
#     print("Voltar e realizar o Checklist! :(")

# #Exercício8
# print("Calculo de atrasos ")
# entregas_agendadas=int(input("Quantidade de entregas agendadas"))
# entregas_atraso=int(input("Quantidade de entregas com atrasos"))
# total=entregas_agendadas / entregas_atraso
# if total>=0.1:
#     print("Necessário Otimizar Rotas")
# else:
#     print("Logistíca Eficiente ")

# #Exercício9
# print("Validação da calibragem")
# carga_pressão=float(input("Digite a medida da pressão em PSI dos Pneus"))
# if carga_pressão <=100:
#     print("Abaixo do recomendado")
# elif carga_pressão>=100:
#     print("Acima do recomendado")
# else:
#     print("Dentro do padrão")

#Exercício10 
# print("Contagem de embarque")
# for embarque in range(5,0,-1):
#  time.slep(1)
# print(f"Embarque em: :) {embarque}")

# #Exercício11
# print("Somatório de frete (Acumulador)")
# faturamento=0
# frete=1

# while frete !=0:
#     frete = float(input("Valor do Frete 0 para encerrar"))
#     faturamento += frete
# print(f"Faturamento total foi de {faturamento}")

# print("Somatório de Frete (Acumulador) - Versão 2.0")
# faturamento = 0 
# while True:
#     valor=float(input("Valor do frete ou 0 para encerrar"))
#     faturamento+=frete
#     print("Faturamento total foi de {faturamento}")

#Exercício12

# print("Monitoramento de frotas")
# maior_km=0
# for i in range(1,6):
#     km= float(input(f"Digite a quilometragem do veiculo{i}"))
#     if km > maior_km:
#         maior_km=km 
# print(f"A maior quilometragem registrada foi de{maior_km} km")

#Exercício 13
# print("Sistema de rastreio")
# erros=0
# tentativas= 3 

# while erros !=3:
#     codiogo=input("Insira o código de acesso")
#     if codigo  != "track99":
#         erros=erros + 1 
#         tentativas=tentativas - 1 
#         print(f"Codigo incorreto voce possui {tentativas}")
#     else:
#         break
#     if erros ==3: 
#         print("Rastreamento bloqueado!")
#     else:
#         print("Acesso liberado :)")

#Exercício 14

# print("Gerenciador de Combustível")
# tanque = 500 
# while True:
#     print("1-Abastecer")
#     print("2- Retirar ")   
#     print("3-Sair") 
#     opção =input("Escolha uma opção")
#     if opção == "1": 
#         valor=float(input("Quantidade a abastecer"))
#         tanque+=valor
#         print(f"Tanque Atual:{tanque}")
#     elif opção =="2":
#         valor=float(input("Quantidade a retirar"))
#         if valor >tanque: 
#          print("Quantidade indisponível ")
#     else: 
#          tanque -= valor 
#          print(f"Tanque Atual{tanque}")
#     elif opção == "3":
#     print("Encerrando o sistema")

#Exercício 15

# contagem = 0
# tatal=5
# for pneu in range(1,6):
#     medida= float(input(f"Medida do sulco do pneu{pneu} em mm "))
#     if medida>=1.6:



