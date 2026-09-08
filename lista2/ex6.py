#6. Detetive do Resto (Operador Módulo % e Condicional)

#O operador % (Módulo) nos devolve o resto da divisão inteira entre dois números. Escreva um programa em Python que:
#I. Solicite ao usuário um número inteiro qualquer através do teclado (lembre-se de usar o int(input()) para converter o dado).
#II. Use a estrutura condicional if/else e o operador % para verificar se o número digitado é PAR ou ÍMPAR.
#(Dica:Todo número par dividido por 2 deixa resto igual a 0. Se o resto for 1, o número é ímpar!)

ni = int(input('Digite um numero inteiro: '));

if ni % 2 == 0:
    print("o numero é par! ");
else:
    print("O numero é impar! ");