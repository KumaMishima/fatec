TEMPORATURA_ATUAL = float(input(f"Digite a temperatura atual: "))
alerta_ativo = TEMPORATURA_ATUAL >= 40.00
print(F"Alerta de superaquecimento ativo: {alerta_ativo}")