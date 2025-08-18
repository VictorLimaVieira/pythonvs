# sorteio

import random 

def sortear_um(alunos):
    return random.choice(alunos)

#programa principal

lista = ['Vicky', 'Joao Pedro', 'Krogues', 'Rickes', 'Victor']
print(f'O aluno escolhido foi {sortear_um(lista)}')