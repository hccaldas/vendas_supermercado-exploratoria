import pandas as pd

def load_and_clean_data(filepath):
    # Carregar os dados
    df = pd.read_csv(filepath)

    # remover os valores nulos
    df.dropna(inplace=True)

    # corrigir os tipos de dados
    df["Date"] = pd.to_datetime(df["Date"])
    df["Total"] = df["Total"].astype(float)

    # criar novas variáveis
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day

    return df

if __name__ == "__main__":
    df = load_and_clean_data("C:\\Users\\Usuário\\predicao_analise\\supermarket_sales - Sheet1.csv")
    print(df.head())
