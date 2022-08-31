# Aula 19 - Dicionários

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