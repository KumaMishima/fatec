#4. O Teste do Tobogã (Operador Lógico or)
#No parque aquático da escola, as regras de segurança para o tobogã gigante são flexíveis para garantir a
#diversão com segurança. Para ter o acesso liberado, o aluno precisa cumprir pelo menos um dos seguintes requisitos:
#I. Ter idade maior ou igual a 12 anos or altura maior ou igual a 1.60 m.
#II. Escreva o programa em Python que receba o nome, a idade e a altura do aluno, faça o teste lógico correto e
#exiba se o acesso foi "Liberado" ou "Bloqueado".

nome = input("Digite seu nome: ");
idade = int(input('Digite sua idade: '));
altura = float(input('Digite a sua Altura: '));

if idade >= 12 or altura >=1.60:
    print(f"{nome} liberado para o tobogã. ");
else:
    print(f"{nome} bloqueado de ir no tobogã. ");