import csv

arquivo = open('cargo.csv')
dados = csv.reader(arquivo, delimiter=',')

tabela = list()

for dado in dados:
    if dado[3] == 'Menor Aprendiz':
        dado.append('Salario base: R$ 850,00')
        tabela.append(dado)

    elif dado[3] == 'Auxiliar':
        dado.append('Salario base: R$ 1.100,00')
        tabela.append(dado)

    elif dado[3] == 'Assistente':
        dado.append('Salario base: R$ 1.674,00')
        tabela.append(dado)
    
    elif dado[3] == 'Coordenador':
        dado.append('Salario base: R$ 5.933,00')
        tabela.append(dado)

    elif dado[3] == 'Diretor':
        dado.append('Salario base: R$ 13.300,00')
        tabela.append(dado)

    else:
        dado.append('salario')
        tabela.append(dado)

novo_arquivo = open('cargo_salario.csv', 'w', newline='')
cargo_salario = csv.writer(novo_arquivo, delimiter=',')
cargo_salario.writerows(tabela)

arquivo.close()
novo_arquivo.close()