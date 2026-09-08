ano_nascimento = int(input(f"Digite seu ano de nascimento: "))
idade = 2026 - ano_nascimento
pode_dirigir = idade >= 18
print(f"Tem permissão para dirigir? {pode_dirigir}")