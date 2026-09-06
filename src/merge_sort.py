"""Merge Sort: O(n log n) nos casos melhor, médio e pior."""


def merge_sort(valores: list[int]) -> list[int]:
    """Ordena a própria lista em ordem crescente e retorna a mesma lista.

    Usa O(n) de memória auxiliar e preserva a ordem dos valores iguais.
    """
    auxiliar = [0] * len(valores)

    def ordenar(inicio: int, fim: int) -> None:
        # O intervalo inclui inicio e exclui fim.
        if fim - inicio <= 1:
            return

        meio = (inicio + fim) // 2
        ordenar(inicio, meio)
        ordenar(meio, fim)

        esquerda, direita = inicio, meio
        destino = inicio

        # Intercala as duas metades já ordenadas.
        while esquerda < meio and direita < fim:
            if valores[esquerda] <= valores[direita]:
                auxiliar[destino] = valores[esquerda]
                esquerda += 1
            else:
                auxiliar[destino] = valores[direita]
                direita += 1
            destino += 1

        while esquerda < meio:
            auxiliar[destino] = valores[esquerda]
            esquerda += 1
            destino += 1

        while direita < fim:
            auxiliar[destino] = valores[direita]
            direita += 1
            destino += 1

        for i in range(inicio, fim):
            valores[i] = auxiliar[i]

    ordenar(0, len(valores))
    return valores


if __name__ == "__main__":
    exemplo = [8, 3, 5, 1, 9, 2]
    print(merge_sort(exemplo))
