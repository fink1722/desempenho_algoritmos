"""Insertion Sort: O(n²) no caso médio/pior e O(n) na entrada ordenada."""


def insertion_sort(valores: list[int]) -> list[int]:
    """Ordena a própria lista em ordem crescente e retorna a mesma lista.

    Usa O(1) de memória auxiliar e preserva a ordem dos valores iguais.
    """
    for i in range(1, len(valores)):
        atual = valores[i]
        j = i - 1

        # Desloca valores maiores para abrir espaço para o valor atual.
        while j >= 0 and valores[j] > atual:
            valores[j + 1] = valores[j]
            j -= 1

        valores[j + 1] = atual

    return valores


if __name__ == "__main__":
    exemplo = [8, 3, 5, 1, 9, 2]
    print(insertion_sort(exemplo))
