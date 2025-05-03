import pandas as pd
from data_clean.data_cleaning import clean_data  # Certifique-se de que o nome da função está correto

# Caminho do arquivo de origem
origin_file = 'origin/customers.csv'

def main():
    try:
        # Passo 1: Ler dados do CSV
        df = pd.read_csv(origin_file)

        # Passo 2: Limpar e validar os dados
        cleanDF = clean_data(df)  # Aqui estamos chamando a função clean_data

        # Passo 3: Salvar os dados limpos nos formatos desejados
        cleanDF.to_csv('output/csv/customers_data_cleaned.csv', index=False)
        cleanDF.to_json('output/json/customers_data_cleaned.json', orient='records', lines=True)
        cleanDF.to_parquet('output/parquet/customers_data_cleaned.snappy.parquet', compression='snappy', index=False)

        print("Data pipeline executed successfully!")

    except Exception as e:
        print(f"Pipeline execution failed with error(s): {e}")

if __name__ == "__main__":
    main()
