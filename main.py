from exploratory_analysis import plot_sales_trend
from model_training import train_and_evaluate_model

if __name__ == "__main__":
    # Atualize o caminho para o arquivo correto
    file_path = "C:\\Users\\Usuário\\predicao_analise\\supermarket_sales - Sheet1.csv"
    
    # Executar as funções
    plot_sales_trend(file_path)
    modelo = train_and_evaluate_model(file_path)