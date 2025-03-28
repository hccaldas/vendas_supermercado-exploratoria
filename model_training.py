import sys
import os

# Adicionar o diretório do projeto ao caminho de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from data_preprocessing import load_and_clean_data

def train_and_evaluate_model(file_path):
    # Carregar e limpar os dados
    df = load_and_clean_data(file_path)
    
    # Selecionar as colunas de entrada (X) e a coluna de saída (y)
    x = df[["Year", "Month", "Day"]]  # Corrigido para usar uma lista de colunas
    y = df["Total"]
    
    # Dividir os dados em conjuntos de treino e teste
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    # Treinar o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(x_train, y_train)
    
    # Fazer previsões e calcular o erro médio absoluto
    predicoes = modelo.predict(x_test)
    erro = mean_absolute_error(y_test, predicoes)
    print(f"Erro Médio Absoluto: {erro}")
    
    return modelo

if __name__ == "__main__":
    # Definir o caminho do arquivo CSV
    file_path = "C:\\Users\\Usuário\\predicao_analise\\supermarket_sales - Sheet1.csv"
    
    # Treinar e avaliar o modelo
    modelo = train_and_evaluate_model(file_path)