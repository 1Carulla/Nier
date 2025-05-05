import sys
import json
import csv
import time
from collections import defaultdict, deque

class AutomatoFinito:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)

        self.initial = data['initial']
        self.final = set(data['final'])
        self.transitions = defaultdict(list)

        for trans in data['transitions']:
            key = (trans['from'], trans['read'])
            self.transitions[key].append(trans['to'])

    def reconhecer(self, palavra)
  
        fila = deque()
        visitado = set()
        fila.append((self.initial, 0))

        while fila:
            estado, pos = fila.popleft()
            if (estado, pos) in visitado:
                continue
            visitado.add((estado, pos))

            if pos == len(palavra) and estado in self.final:
                return True
              
            if pos < len(palavra):
                letra = palavra[pos]
                for prox in self.transitions.get((estado, letra), []):
                    fila.append((prox, pos + 1))

            for prox in self.transitions.get((estado, None), []):
                fila.append((prox, pos))

        return False
def executar_testes(automato_path, testes_path, saida_path):
    automato = AutomatoFinito(automato_path)

    with open(testes_path, 'r') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    resultados = []

    for linha in linhas:
        cadeia, esperado = linha.split(';')
        esperado = int(esperado)

        inicio = time.time()
        obtido = 1 if automato.reconhecer(cadeia) else 0
        fim = time.time()
        duracao = round(fim - inicio, 5)

        resultados.append(f"{cadeia};{esperado};{obtido};{duracao}")

    with open(saida_path, 'w') as f:
        f.write("\n".join(resultados))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python simulador.py <arquivo_automato.aut> <arquivo_testes.in> <arquivo_saida.out>")
        sys.exit(1)

    arquivo_aut = sys.argv[1]
    arquivo_in = sys.argv[2]
    arquivo_out = sys.argv[3]

    executar_testes(arquivo_aut, arquivo_in, arquivo_out)
