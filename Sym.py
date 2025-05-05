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
