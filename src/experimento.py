"""Executa as medições e salva uma tabela CSV e um gráfico."""
import csv
import random
from pathlib import Path
from statistics import median
from time import perf_counter

import matplotlib.pyplot as plt

from insertion_sort import insertion_sort
from merge_sort import merge_sort


def main(pasta=Path(__file__).resolve().parent.parent):
    tamanhos = [2000, 4000, 8000, 16000, 32000]
    gerador = random.Random(42)
    algoritmos = [("Insertion Sort", insertion_sort), ("Merge Sort", merge_sort)]
    resultados = []
    anteriores = {}

    for n in tamanhos:
        aleatoria = list(range(n))
        gerador.shuffle(aleatoria)

        for cenario, entrada in [("Aleatória", aleatoria), ("Ordenada", sorted(aleatoria))]:
            for nome, ordenar in algoritmos:
                tempos = []
                esperado = sorted(entrada)
                for execucao in range(4):
                    copia = entrada.copy()  # Cada execução recebe a entrada original.
                    inicio = perf_counter()
                    ordenar(copia)
                    tempo = perf_counter() - inicio
                    assert copia == esperado  # Conferência fora do tempo medido.
                    if execucao > 0:  # Descarta a primeira execução.
                        tempos.append(tempo * 1000)

                mediana = median(tempos)
                chave = (nome, cenario)
                razao = mediana / anteriores[chave] if chave in anteriores else ""
                anteriores[chave] = mediana
                resultados.append([nome, cenario, n, *tempos, mediana, razao])
                print(f"{nome}, {cenario}, n={n}: {mediana:.3f} ms", flush=True)

    (pasta / "dados").mkdir(exist_ok=True, parents=True)
    with (pasta / "dados" / "tempos.csv").open("w", newline="", encoding="utf-8") as arquivo:
        tabela = csv.writer(arquivo)
        tabela.writerow(["algoritmo", "cenario", "n", "tempo1_ms", "tempo2_ms", "tempo3_ms", "mediana_ms", "razao"])
        tabela.writerows(resultados)

    for nome, _ in algoritmos:
        for cenario in ["Aleatória", "Ordenada"]:
            pontos = [r for r in resultados if r[0] == nome and r[1] == cenario]
            plt.plot(tamanhos, [r[6] for r in pontos], marker="o", label=f"{nome} - {cenario}")

    plt.yscale("log")  # Permite enxergar os casos rápidos e lentos juntos.
    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Mediana do tempo (ms, escala logarítmica)")
    plt.title("Insertion Sort e Merge Sort")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    (pasta / "graficos").mkdir(exist_ok=True, parents=True)
    plt.savefig(pasta / "graficos" / "comparacao.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
