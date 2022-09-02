brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

# ==== ACRESCENTAR ELEMENTOS NO DICIONÁRIO USANDO ESTRUTURA DE REPETIÇÃO ==== #
estado = dict()
brazil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
# MÉTODO COPY FAZ A ADIÇÃO (CÓPIA) PRA DENTRO DO DICIONÁRIO
    brazil.append(estado.copy())
print(brazil)

for e in brazil:
    for k, v in e.items():
        print(f'{k} = {v}')

for e in brazil:
    for v in e.values():
        print(v, end=' ')
    print()