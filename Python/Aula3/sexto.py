# #Lista de temperatura lidas pelo sensor por minuto 
# leituras = [70,75,82,98,110,85,80]

# for temp in leituras: 
#     if temp > 100:
#         print(f"CRÍTICO:{temp}°C detectado! Acionando parada de emergencia.")
#     break # O loop para aqui e NÃO le os proximos valores (85 e 80)
#     for temp1 in baixos:
#         if temp1< 50: 
#             print(f"temperatura esta em {temp} C.operação normal.")

#     print("Sistema desligado,Aguardando manutenção.")
    
# #Exercício 2
# for temp in leituras:
#     if temp > 100: 
#         print(f"CRÍTICO:{temp}°C detectado!Acionado parada de emergência.")
#         break #O loop  para aqui e NÃO lê os próximos valores (85 ,80)

# materiais =[ "metal","metal","plastico", "metal", "vidro","metal"]
# for peca in materiais: 
#     if peca != "metal":
#         print(f"Aviso:Peça de {peca} detectada. Desviando para descarte... ")
#         continue #Pula o restante do código abaixo e vai para a próxima peça 

# #Este código só roda se a peça for de metal
# print(f"Processando peça de {peca}.Furando e polindro...")

# print("Fim do lote de produção.")

# Exercício 1 
# Tente criar um código que conte 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma alha de sensor específica no item 5).
# from time import sleep
# for num in range(1,11):
#     if num == 5: 
#         print(f"Falha ao imprimir o n° {num}")
#         sleep(1.8)
#         continue 
#     print(f"Listando números{num}")
#     sleep(2)
#     print("Fim!")


#Exercício 2 
#Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa 

# from time import sleep 
# for i in range(1,11):
#     sleep (0.5)
#     print("Verde")
#     print("Siga em frente") 

#Exercíco 3 - Soma de Cargas de Energia (For)
# Uma fábrica tem 5 máquinas. Peça ao usúario (via input dentro do loop) o consumo em kwh de cada uma das 5 máquinas. Ao final do loo, o programador deve exibir o consumo total da fábrica 
# total=0 
# i= 0 
# for máquinas in range (1,6):
#   consumo=float(input(f"digite o consumo da máquina {i} (em kwh):"))
# total+consumo
# print(f"consumo total da fabrica{total} kwh")

#Exercício 4 - Identificador de peças defeituosoas
# medidas= [50.1,49.8,52.0,48.5]
# for pecas in medidas:
#    if pecas > 50:
#       print(f"Peça {pecas} Aprovada..:)")
#    else: 
#       print(f"Peça {pecas} Rejeitada")

      