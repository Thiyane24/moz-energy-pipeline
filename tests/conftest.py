import pytest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Country Name': ['Mozambique'] * 6,
        'Country ISO3': ['MOZ'] * 6,
        'Year': [1985, 1990, 2000, 2010, 2020, 2021],
        'Indicator Name': [
            'Access to electricity, urban (% of urban population)',
            'Access to electricity, rural (% of rural population)',
            'Energy imports, net (% of energy use)',
            'Access to electricity, urban (% of urban population)',
            'Access to electricity, rural (% of rural population)',
            'Energy imports, net (% of energy use)',
        ],
        'Value': [60.0, 5.0, -3.5, 71.0, 11.0, 2.0]
    })