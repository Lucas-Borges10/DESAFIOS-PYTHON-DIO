import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel('pasta1.xlsx', engine='openpyxl')
planilha = planilha.rename(columns={"nome":"sobrenome"})

print(planilha.shape) #total de linhas e colunas
print(planilha.columns) #nome das colunas
print(planilha.head(2)) #retorna a quantidade de linhas que eu quero
print(planilha.describe()) #retorna dados estátisticos
planilha["Sobrenome"] = "Custódio", "Bonifácio", "Tereza" #cria outra coluna




