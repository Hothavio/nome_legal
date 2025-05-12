from analise import analisar_lista

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

resultado = analisar_lista(numeros)

print("Resultado da análise:\n")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
