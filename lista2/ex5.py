#5. Peneira do Vôlei (Condicional Simples if/else)
#O treinador do time de vôlei da escola estipulou que, para participar da seleção masculina/feminina, o
#candidato deve medir pelo menos 1.70m de altura. Escreva um programa que peça a altura do aluno e
#exiba se ele está "Aprovado para o teste" ou "Classificado para outras modalidades".
#Uso do operador relacional de maior ou igual (>=) e a conversão da entrada para número real (float).

altura = float(input('Digite sua altura: '));

if altura >= 1.70:
    print("Aprovado");
else:
    print("Classificado para outras modalidades. ");