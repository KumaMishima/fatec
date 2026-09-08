#7. Classificação de Triângulos (Aritmética, Relacionais e Lógica)
#Para construir um triângulo, a regra matemática diz que a soma de dois lados deve ser sempre maior que o
#terceiro lado. Peça ao usuário para digitar três valores inteiros: ladoA, ladoB e ladoC.
#I. Primeiro, verifique se os lados formam um triângulo válido usando o operador and:
#o if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
#II. Se for um triângulo válido, use o if/elif/else para classificá-lo:
#o Equilátero: Se todos os lados forem iguais (ladoA == ladoB and ladoB == ladoC).
#o Isósceles: Se pelo menos dois lados forem iguais.
#o Escaleno: Se todos os lados forem diferentes.
#III. Se a primeira validação for falsa, o programa deve exibir: "Os valores não podem formar um triângulo!"

ladoA = int(input("Digite o valor do lado A: "));

ladoB = int(input("Digite o valor do lado B: "));

ladoC = int(input("Digite o valor do lado C: "));


if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):
    if (ladoA == ladoB and ladoB == ladoC):
        print("O triangulo é um Equilátero. ");
    elif (ladoA == ladoB or ladoB == ladoC or ladoA == ladoC):
        print("O triangulo é um Isósceles. ");
    else:
        print("Os valores formaram um triangulo Escaleno ");