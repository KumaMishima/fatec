#Exercício 2: Menu Interativo de Atendimento (SAC)
#Monte o menu de um robô de atendimento. Mostre na tela as opções: 1 - Suporte Técnico, 2 -
#Financeiro, 3 - Falar com Atendente. Solicite que o usuário digite a opção desejada. Exiba para qual setor a
#chamada está sendo transferida ou diga "Opção inválida" se for digitado algo fora do menu.

setor = {
    1: "Suporte Técnico",
    2: "Financeiro",
    3: "Falar com o atendente"
}

print("----Atendimento-----")
print("1 - Suporte Técnico")
print("2 - Financeiro")
print("3 - Falar com o Atendente")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print("Redirecionando para o Suporte Técnico")
    case 2:
        print("Redirecionando para o Financeiro")
    case 3:
        print("Redirecionando para o atendimento...")
    case _:
        print("Opção Inválida")
