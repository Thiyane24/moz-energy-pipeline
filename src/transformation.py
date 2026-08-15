import pandas as pd
from datetime import datetime


class Transformation:
    def __init__(self, df):
        self.df = df

    def filter(self):
        self.df = self.df[self.df['year'] >= 1990]
        return self

    def standardize(self):
        self.df.columns = self.df.columns.str.replace(' ', '_').str.lower()
        return self

    def flag_negative_values(self):
        self.df['is_net_energy_exporter'] = self.df['energy_imports_net__of_energy_use'] < 0
        return self

    def pivot_table(self):
        self.df = self.df.pivot(index='year', columns='indicator_name', values='value')
        self.df.columns.name = None
        self.df = self.df.reset_index()
        self.df.columns = self.df.columns.str.replace(' ', '_').str.lower().str.replace(r'[^a-z0-9_]', '', regex=True)
        return self

    def save_to_parquet(self, load_id=None):
        if load_id is None:
            load_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f'Data/silver/energy-and-mining_moz_{load_id}.parquet'
        self.df.to_parquet(path, index=False)
        print(f"Data transformed and saved to {path}")
        return self