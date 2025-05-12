def analisar_lista(numeros):
    if not numeros:
        return "A lista está vazia."

    quantidade = len(numeros)
    soma_total = sum(numeros)
    media = soma_total / quantidade
    maior = max(numeros)
    menor = min(numeros)
    pares = len([n for n in numeros if n % 2 == 0])


    return {

        "Média": media,
        "Maior Número": maior,
        "Menor Número": menor,
        "Pares": pares

    }


numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
resultado = analisar_lista(numeros)


for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
