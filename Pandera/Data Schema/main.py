import pandas as pd
import pandera as pa
from pandas import DataFrame
from pandera.typing import DataFrame
import dataframe_schema_class as dsc
import dataframe_schma as ds


# Extrait des données
@pa.check_types(lazy=True)
def get_csv_data_check_with_class_schema(csv_file: str) -> DataFrame | None:
    try:
        df = pd.read_csv(csv_file)
        df['rank'] = df['rank'].fillna(0)
        df['rank'] = df['rank'].astype('int64')
        return df
    except Exception as e:
        print(e)
        return None


def get_csv_data_check_with_schema(csv_file: str) -> DataFrame | None:
    try:
        df = pd.read_csv(csv_file)
        df['rank'] = df['rank'].fillna(0)
        df['rank'] = df['rank'].astype('int64')
        ds.japanese_prefectures_data_schema(df)
        return df
    except Exception as e:
        print(e)
        return None


def main() -> None:
    # japanese_prefectures_data = get_csv_data_check_with_class_schema(csv_file='List_of_Japanese_prefectures_by_GDP.csv')
    japanese_prefectures_data = get_csv_data_check_with_schema(csv_file='List_of_Japanese_prefectures_by_GDP.csv')
    print(japanese_prefectures_data)


if __name__ == "__main__":
    main()
