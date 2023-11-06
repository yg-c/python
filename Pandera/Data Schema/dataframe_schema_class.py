import pandera as pa
from pandera.typing import DataFrame, Series
from pandera import DataFrameSchema, Column, Check, Index, MultiIndex


class JapanesePrefecturesData(pa.SchemaModel):
    """Schema pour List_of_japanese_prefectures_by_GDP.csv"""
    prefecture: Series[str]
    rank: Series[int] = pa.Field(nullable=True)
    yen_2014: Series[int]
    usd_2014: Series[int]
    percent: Series[float]
