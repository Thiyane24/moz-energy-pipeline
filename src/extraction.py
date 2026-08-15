from datetime import datetime
import pandas as pd

def extract():
    df = pd.read_csv('Data/energy-and-mining_moz.csv', sep=',', encoding='utf-8')

    load_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f'Data/bronze/energy-and-mining_moz_{load_id}.parquet'
    df.to_parquet(path, index=False)
    print(f"Data extracted and saved to {path}")

    return df, load_id