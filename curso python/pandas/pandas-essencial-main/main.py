# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:27:46 2024

@author: alanm
"""

import pandas as pd

data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';') #header=None remove the names of the coloums

#data.head(n) retorna um dataframe com as 'n' primeiras posições do dataframe original
#data.tail(n or None=5) msm coisa só que no final do dataframe
#data.info() informações do dataframe

# series
print(data.head)
print(data['ESTADO']) 
#ou
#print(data.ESTADO) # nome não pode ter nenhum caractere especial ou espaço

#linha n
#print(data.iloc[n])
print(data.iloc[1])

#criar Series

series1 = pd.Series([0, 2, 4, 6], index=['linha1', 'linha2', 'linha3', 'linha4'])
print(series1)


produto_view = data['PRODUTO'] # é uma referencia e não copia

#print(produto_view)

#copia

produto_view_bckup = data['PRODUTO'].copy()

#print(produto_view_bckup)

#shape retorna uma tuple

nrows, ncols = data.shape

print(f'{nrows}, {ncols}.')

novos_produtos = [f'Produto {i}' for i in range(nrows)]
#print(novos_produtos)

print(data.shape, len(novos_produtos))

#tem q ser do msm tamanho
data['PRODUTO'] = novos_produtos

produto_view[0] = 0
#alterar uma view q é referencia altera no dataframe tbm mas alterar no dataframe não altera na view

print(data['PRODUTO'])
print(produto_view)
print(produto_view_bckup)


#criando colunas
#com valor default
#data['Teste'] = 'DEFAULT'
#print(data)

#criar coluna preço medio de coluna em dolares (não faz mt sentido mas é para teste)

data['PREÇO MÉDIO REVENDA EM DOLARES'] = data['PREÇO MÉDIO REVENDA'] * 5.0
print(data['PREÇO MÉDIO REVENDA EM DOLARES'], data['PREÇO MÉDIO REVENDA'])


satisfacao_cliente = pd.DataFrame({
    'boas' : (10, 2, 5),
    'medias' : (20, 18, 5),
    'pessimas' : (0, 10, 20)
}, index=('PlayStation', 'Xbox', 'Nintendo'))

print(satisfacao_cliente)

#10 a 15
print(data.iloc[10:16])

print(data.iloc[[1, 5, 10, 15]])

#indice e coluna

print(data.iloc[1, 4]) #Goias

#loc - label based selection

#retorna linha playstation
print(satisfacao_cliente.loc['PlayStation'])

#retorna a quantidade avaliações pessimas da linha playstation
print(satisfacao_cliente.loc['PlayStation', 'pessimas'])

#retorna as linha selecionadas
print(satisfacao_cliente.loc[['PlayStation', 'Xbox']])

#apenas colunas bom e pessimas

print(satisfacao_cliente.loc[:, ['boas', 'pessimas']])

#
print(data[['ESTADO', 'DATA INICIAL', 'REGIÃO']])

#remover colunas

print(data.head())
del data['PREÇO MÉDIO REVENDA EM DOLARES']

print(data.head())

del data['Unnamed: 0']

print(data.head())

data.to_csv(r'./datasets/GasPricesinBrazil_2004-2019_preprocessado.csv', index=False)

print(data)