import duckdb
import pandas as pd


def load_gold(silver_path: str):
    df = pd.read_parquet(silver_path)
    df['urban_rural_gap'] = (
        df['access_to_electricity_urban__of_urban_population']
        - df['access_to_electricity_rural__of_rural_population']
    )

    con = duckdb.connect('Data/gold/pipeline.duckdb')
    con.execute("CREATE TABLE IF NOT EXISTS energy_gold AS SELECT * FROM df")
    con.execute("INSERT INTO energy_gold SELECT * FROM df")
    con.close()

    print("Gold layer written to Data/gold/pipeline.duckdb")