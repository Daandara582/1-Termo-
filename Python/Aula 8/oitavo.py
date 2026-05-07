#Clean Code - Aula 8 
#Para que Usar?
#Como usar?
# print("Clean Code- Aula 8")
# aula=8
# print(f"Estamos na aula {aula} de Clean Code ")

#Manipulação de arquivos e Texto 
# manipulação_arquivos="Manipulação de arquivos e Texto com Python"
# print(manipulação_arquivos.upper()) #Maiúsculas 
# print(manipulação_arquivos.lower()) #Minusculas 
# print(manipulação_arquivos.strip()) #Remove espaços em branco 
# print(manipulação_arquivos.split()) #Divide a String em uma lista de palavras
# print(manipulação_arquivos.replace("Python","Java")) #Substitui "Espaço" por "Java"
# print(manipulação_arquivos.replace(" ","_")) #Substitui "Espaço" por "_"
# print(manipulação_arquivos.count("a")) #Conta quantas vezes a letra "a" aparece na string
# print(manipulação_arquivos.count("Python")) #Conta quantas vezes a palavra "Python" aparece na string
# print(manipulação_arquivos.upper().count("PYTHON")) #Conta quantas vezes a letra "PYTHON" aparece na string e 
# print(manipulação_arquivos.strip().count("python")) #Conta quantas vezes 
# print(manipulação_arquivos.find("Python"))

# print(manipulação_arquivos.title())
# print(manipulação_arquivos.capitalize())
# print(manipulação_arquivos.swapcase())
# print(manipulação_arquivos.center(50, "*"))
# print(manipulação_arquivos.startswitch("     Manipulação"))

#Exercício 1 
# frase_Usuário=input("Inserir frase :)")
# print(frase_Usuário.upper())
# print(frase_Usuário.count(frase_Usuário))
# print(frase_Usuário.count(""))

#Manipulação de arquivos 
#Escrevendo em um arquivo
# with open ("arquivo.txt","w") as exemplo:
#     exemplo.write("Exemplo de Clean Code - Aula 8\n")
#     exemplo.write("Continuando a escrever no arquivo\n")
# # w = write - Escreve no arquivo,se o arquivo já existir,ele irá sobreescrever o conteudo 

# with open ("arquivo.py", "w") as python:
#     python.write('print("Exemplo de arquivo Python")')

# #Lendo um arquivo 
# with open ("arquivo.txt","r") as exemplo:
#     conteudo=exemplo.read()
#     print(conteudo)

#Lendo um arquivo 
# with open("arquivo.py","r") as python:
#     conteudo=python.read()
#     print(conteudo)

# with open("arquivo.py", "a") as python:
#     python.write('\nprint("Continuando a escrever no arquivo Python")')


import os

#Criando um diretório 
# os.mkdir("Teste")

# #Renomear pastas 
# os.rename("Teste","Aulas")

#Excluir pastas 
# os.rmdir("Aulas")

#Criar arquivos 
# os.mknod("teste.txt")
# os.touch("aula.txt")

#Listagem de Diretórios
# print(os.listdir()) #Lista os arquivos e pastas do diretório atual
# print(os.listdir(". .")) #Lista os arquivos e pastas do diretório pai 
# print(os.listdir("C:\\")) #Lista os arquivos e pastas do diretório raiz do C

#Exercício 2 
# with open("desligar.bat","w") as desligar:
#     desligar.write("shutdown /s /t 0 /c""Sextou! Pode descansar")

# #Exercício 3
# with open("cancelar.bat","w") as cancelar:
#     cancelar.write("shutdown /a")

# #Exercício 4
# print("Arquivos do diretório atual:")
# print(os.listdir())

#Exercício 5















