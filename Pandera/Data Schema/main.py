import pandas as pd
import pandera as pa
from pandera.typing import DataFrame
import dataframe_schema_class as ds


# Extrait des données
@pa.check_types(lazy=True)
def get_csv_data(csv_file: str) -> DataFrame[ds.JapanesePrefecturesData]:
    df = pd.read_csv(csv_file)
    df['rank'] = df['rank'].fillna(0)
    df['rank'] = df['rank'].astype('int64')
    return df


def main() -> None:
    try:
        japanese_prefectures_data = get_csv_data(csv_file='List_of_Japanese_prefectures_by_GDP.csv')
        print(japanese_prefectures_data)
    except pa.errors.SchemaErrors as schema_error:
        print(schema_error)


if __name__ == "__main__":
    main()
