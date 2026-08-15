from src.extraction import extract
from src.transformation import Transformation
from src.loading import load_gold


def main():
    # Bronze
    df, load_id = extract()

    # Silver
    silver_path = f'Data/silver/energy-and-mining_moz_{load_id}.parquet'
    (
        Transformation(df)
        .standardize()
        .filter()
        .pivot_table()
        .flag_negative_values()
        .save_to_parquet(load_id)
    )

    # Gold
    load_gold(silver_path)


if __name__ == "__main__":
    main()