# Aula 19 - Dicionários
# CURSO GIT - PAREI EM 25M18S: https://www.youtube.com/watch?v=5BYm7UdCrX0
# AULA 19 - PAREI EM  9M56S: https://www.youtube.com/watch?v=ZWj8o692qGY&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=22

# Para criar um dicionário uso as {}
dados = {'nome': 'Pedro', 'idade': 25}

# Adicionando um elemento no dicionário
dados['sexo'] = 'M'
del dados['idade']

print(dados.values())

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
        }
# Exibe o conteúdo de cada elemento do dicionário
print(filme.values())

# Exibe os índices dos elementos do dicionário
print(filme.keys())

# Exibe os valores e os índices do dicionário
print(filme.items())

for k, v in filme.items():
    print(f'0 {k} é {v}')

print('\n# ---------- EXERCÍCIOS ---------- #\n')

pessoas = {'nome': 'Ezequiel', 'sexo': 'M', 'idade': 38}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')