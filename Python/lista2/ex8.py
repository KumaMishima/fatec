#8. O Alerta da Estufa de Biologia (Condicionais if, elif e else)
#O laboratório de ciências possui uma estufa automatizada para plantas tropicais sensíveis. O sistema de
#monitoramento precisa ler a temperatura atual e disparar um alerta visual na tela para que os alunos saibam
#se as condições físicas do ambiente estão adequadas.
#I. Temperaturas abaixo de 15.0 °C são classificadas como "Muito Frio".
#II. Temperaturas entre 15.0 °C e 25.0 °C (inclusive) são classificadas como "Temperatura Ideal".
#III. Temperaturas acima de 25.0 °C são classificadas como "Muito Quente".
#Escreva o programa em Python que solicite a temperatura medida (float). Usando a estrutura de decisão, exiba na
#tela o status correspondente para alertar o operador da estufa.

temperatura_atual = float(input('Digite a temperatura atual: '));

if temperatura_atual <15.0:
    print("Muito Frio. ");
elif temperatura_atual <= 25.0:
    print("Temperatura Ideal. ");
else:
    print("Muito Quente! ")