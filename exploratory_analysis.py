import pandas as pd
import matplotlib.pyplot as plt

def plot_sales_trend(file_path):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(file_path)
    
    # Verificar se as colunas necessárias existem
    if not {"Date", "Total"}.issubset(df.columns):
        raise ValueError("O arquivo CSV deve conter as colunas 'Date' e 'Total'.")
    
    # Converter a coluna 'Date' para o formato datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    
    # Agrupar os dados por data e somar as vendas totais
    sales_trend = df.groupby('Date')['Total'].sum()
    
    # Plotar a tendência de vendas
    plt.figure(figsize=(10, 6))
    sales_trend.plot(kind="line", marker="o")
    plt.title("Tendência de Vendas ao Longo do Tempo")
    plt.xlabel("Data")
    plt.ylabel("Vendas Totais")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Atualize o caminho para o arquivo correto
    plot_sales_trend("C:\\Users\\Usuário\\predicao_analise\\supermarket_sales - Sheet1.csv")