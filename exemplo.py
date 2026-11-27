import pandas as pd 

idades_lista = [25, 30, 22, 28]
idades_series = pd.Series([25, 30, 22, 28]) 

#print(f"Lista:\n{idades_lista}\n")
#print(f"Series:\n{idades_series}\n")

# Manipulando series e consultas
notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana' ])

#print(notas['Maria'])     #Acessando a nota de Maria pelo rotulo
#print(notas.iloc[2])      #Acessando a nota de Pedro pela Posição   
#print(notas.mean())       #Calculando a média das notas  
#print(notas[notas > 8])   #Filtrando notas maires que 8   
#print(notas.describe())   #Estatísticas descritivas das notas

# Operaçoes aritméticas e entre duas series 

#Aumenta todas as notas em 10% de uma vez só

notas_ajustadas = notas * 1.10
print(notas_ajustadas)

# Comparar com uma segunda serie
notas_exame_final = pd.Series([10, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana' ])
diferenca = notas_exame_final - notas_ajustadas

print(diferenca)

# DAtaFremes: Lendo planilhas do exel 

df = pd.read_excel('base_invest.xlsx') # Lé a planilha exel da pasta 

print(df.head())                       # Exibe as 5 primeiras linhas 

# Abrir abas de planilhas do execel diferentes
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')

df_ativos = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

print(df_transacoes.head())
print(df_ativos.head())