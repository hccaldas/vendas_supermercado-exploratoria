# Predição e Análise de Vendas de Supermercado

Este projeto realiza uma análise exploratória de dados (EDA) e treina um modelo de regressão linear para prever vendas com base em dados históricos de um supermercado. O projeto utiliza bibliotecas populares de Python para manipulação de dados, visualização e aprendizado de máquina.

## Estrutura do Projeto

predicao_analise/ 
├── exploratory_analysis.py # Contém a função para análise exploratória (plot_sales_trend) 
├── model_training.py # Contém a função para treinar e avaliar o modelo (train_and_evaluate_model) 
├── data_preprocessing.py # Contém a função para carregar e limpar os dados (load_and_clean_data) 
├── main.py # Arquivo principal para executar o pipeline completo 
├── supermarket_sales - Sheet1.csv # Arquivo de dados de vendas do supermercado 
├── requirements.txt # Lista de dependências do projeto 
└── README.md # Documentação do projeto


## Funcionalidades

1. **Análise Exploratória de Dados (EDA)**:
   - A função `plot_sales_trend` no arquivo `exploratory_analysis.py` gera um gráfico de linha mostrando a tendência de vendas ao longo do tempo.

2. **Treinamento de Modelo**:
   - A função `train_and_evaluate_model` no arquivo `model_training.py` treina um modelo de regressão linear para prever o total de vendas com base em variáveis como preço unitário e quantidade.

3. **Pré-processamento de Dados**:
   - A função `load_and_clean_data` no arquivo `data_preprocessing.py` carrega e limpa os dados, removendo valores nulos e preparando o DataFrame para análise e modelagem.

## Como Executar o Projeto

### 1. Clone o Repositório


(Crie um Ambiente Virtual (Opcional, mas Recomendado))
No Windows:

    python -m venv venv
    venv\Scripts\activate

No Linux/Mac:

    python3 -m venv venv
    source venv/bin/activate

Instale as Dependências

    pip install -r requirements.txt

Execute o Script Principal

    python [main.py](http://_vscodecontentref_/1)

Resultados
Um gráfico de linha será exibido mostrando a tendência de vendas ao longo do tempo.
O erro médio absoluto (MAE) do modelo será exibido no terminal.
Dependências
As dependências do projeto estão listadas no arquivo requirements.txt. Certifique-se de instalá-las antes de executar o projeto.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está sob a licença MIT.



