total_vagas= 500 
vagas_ocupadas= 499 

print("Bem vindo ao Shopping!")
entrada = input("Qual a forma de entrada? ticket ou tag")
if entrada == "ticket":
    print("Retire seu ticket")
elif entrada == "tag":
    print("Sua entrada será registrada")
else:
    print("Sua entrada foi registrada")

if total_vagas >=500:
    print("Estacionamento lotado ")
elif total_vagas <=500:
    print(" Estacionamento livre")
    