import pandas as pd


tabela = pd.read_excel('Produtos.xlsx')

tabela.loc[tabela['Tipo']== 'Serviços', 'Multiplicador Imposto'] = 1.5

#Coluna 'Preço Base Reais' recebe novo calculo:
tabela['Preço Base Reais'] = tabela['Multiplicador Imposto'] * tabela['Preço Base Original']

# Se der o mesmo nome do xlsx original; ele Salva e Substituindo o Arquivo .xlsx Original:
# tabela.to_excel('Produtos.xlsx')
tabela.to_excel('Produtos_Made_In_Pandas.xlsx')

tabela2 = pd.read_excel('Produtos_Made_In_Pandas.xlsx')

print(tabela2)
