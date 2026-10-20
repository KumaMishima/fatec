#2. O Mensageiro de Boas-Vindas (Concatenação)
#Escreva um programa em Python que solicite ao usuário o seu nome e a sua idade. O programa deve exibir na tela a
#mensagem: "Olá (Nome), você tem (Idade) anos!".
#Resolver este exercício usando concatenação (+), e realizar a conversão usando str()

nome = input("Digite seu nome: ");
idade = int(input("Qual a sua Idade? "));

print(f"Olá {nome}! você tem {idade} anos!");