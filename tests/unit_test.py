import pytest
import pandas as pd
from src.transformation import Transformation


def test_filter_removes_pre_1990(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    assert t.df['year'].min() >= 1990

def test_filter_keeps_post_1990(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    assert len(t.df) > 0


def test_standardize_renames_columns_to_snake_case(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    for col in t.df.columns:
        assert ' ' not in col
        assert col == col.lower()


def test_flag_negative_values_correct(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    t.pivot_table()
    t.flag_negative_values()
    assert 'is_net_energy_exporter' in t.df.columns


def test_flag_negative_marks_exporter(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    t.pivot_table()
    t.flag_negative_values()
    # 2010 row: energy imports net = 2.0 (positive) → not exporter
    row_2010 = t.df[t.df['year'] == 2010]
    assert row_2010['is_net_energy_exporter'].values[0] == False


def test_pivot_table_has_year_as_column(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    t.pivot_table()
    assert 'year' in t.df.columns


def test_pivot_table_one_row_per_year(sample_df):
    t = Transformation(sample_df)
    t.standardize()
    t.filter()
    t.pivot_table()
    assert t.df['year'].is_unique


def test_chaining_returns_self(sample_df):
    t = Transformation(sample_df)
    result = t.standardize().filter().pivot_table().flag_negative_values()
    assert isinstance(result, Transformation)