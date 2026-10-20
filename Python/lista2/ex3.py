#3. Triagem de Exame (Operador Lógico and)
#Em hospitais, antes de aplicar certos tipos de medicamentos de contraste, é necessário fazer uma triagem
#de segurança. Escreva um programa que peça o nome, a idade (Inteiro) e o peso (float) de um paciente. O
#paciente só estará liberado para o exame se atender a duas condições simultaneamente:
#I. Ter idade maior ou igual a 18 anos and peso maior ou igual a 50.0 kg.
#II. Se atender aos requisitos, exiba: "Paciente {Nome} liberado para o exame de contraste."
#III. Senão, exiba: "Alerta! Paciente {Nome} necessita de avaliação médica especial."

nome = input("Digite seu nome: ");
idade = int(input('Digite sua idade: '));
peso = float(input('Digite seu peso: '));

if idade >= 18 and peso >=50:
    print(f"paciente {nome} liberado para fazer o exame de contraste. ");
else:
    print(f"Alerta! Paciente {nome} necessita de avaliação médica especial. ");