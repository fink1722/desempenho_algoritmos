# Diário

## Antes de medir

Esperávamos que, ao dobrar o tamanho, o tempo do Insertion Sort aumentasse cerca de 4 vezes na entrada aleatória e 2 vezes na ordenada. Para o Merge Sort, esperávamos um pouco mais de 2 vezes nos dois cenários.

## Dificuldades e ajustes

A primeira versão usava repetições internas e ficou complicada. Simplificamos para quatro execuções por ponto: descartamos a primeira e usamos a mediana das três restantes. Aumentamos os tamanhos para 2.000, 4.000, 8.000, 16.000 e 32.000 para reduzir o efeito do ruído, embora os casos ordenados ainda sejam rápidos.

Foi necessário instalar Matplotlib para gerar o gráfico. O Insertion Sort aleatório demorou mais nos maiores tamanhos: em 32.000 elementos, sua mediana foi de aproximadamente 22,6 segundos por execução.

## Depois de medir

As razões ficaram próximas das previsões: entre 3,90 e 4,11 para Insertion Sort aleatório; entre 2,00 e 2,03 para Insertion Sort ordenado; e entre 2,03 e 2,26 para Merge Sort nos dois cenários.

Todas as saídas foram conferidas e estavam ordenadas. Mantivemos as oscilações medidas. A semente 42 reproduz as entradas, mas os tempos podem mudar com a carga do computador. A tabela do README e o CSV registram esta execução.
