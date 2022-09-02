aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 7:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'
print(f'A situação de {aluno["nome"]} é {aluno["situação"]}')