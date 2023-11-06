import pandera as pa

japanese_prefectures_data_schema = pa.DataFrameSchema({
    'prefecture': pa.Column(pa.String),
    'rank': pa.Column(pa.Int, nullable=True),
    'yen_2014': pa.Column(pa.Int),
    'usd_2014': pa.Column(pa.Int),
    'percent': pa.Column(pa.Float, checks=pa.Check.less_than_or_equal_to(max_value=100))
})
