# Nier
Trabalho do grande professor Dellamura

# Simulador de Autômatos Finitos

Este projeto simula um simulador de autômatos finitos

A ferramenta funciona via linha de comando e processa arquivos de entrada contendo a definição do autômato e uma lista de testes, gerando um relatório com os resultados.

O simulador percorre os estados do autômato usando busca em largura, considerando todas as transições possíveis(afd/afbd) (inclusive null, que representam ε-movimentos).
A entrada é aceita se houver algum caminho que consuma toda a cadeia e termine em um estado final.
O algoritmo funciona para autômatos determinísticos e não determinísticos.


```bash
python simulador.py automato_exemplo.aut testes_exemplo.in resultados.out
