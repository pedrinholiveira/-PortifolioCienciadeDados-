import pandas as pd

def data_input(path_file: str, type="csv" or "xlsx"):
    """
    Lê um arquivo csv ou excel e retorna um dataframe do Pandas

    Argumentos: 
        path_file (str): O caminho completo do arquivo CSV, incluindo o nome e a extensão do arquivo.
    Returns:
        Retorna None se o arquivo não for encontrado, e caso for encontrado retorna o dataframe
    """
    try:
        if path_file.endswith(".csv"):
            df = pd.read_csv(f"{path_file}")
        elif path_file.endswith(".xlsx"):
            df = pd.read_excel(f"{path_file}")
        else:
            print("O arquivo não esta no formato adequado. Utilize csv ou xlsx")
            return None
        return df
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print(f"erro: {e}")
        return e

    
          