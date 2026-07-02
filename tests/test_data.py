from data import load_campaign_data


def test_load_campaign_data_returns_typed_dataframe():
    df = load_campaign_data()

    assert list(df.columns) == [
        "date", "channel", "campaign", "spend", "conversions",
        "revenue", "creative_name", "ctr",
    ]
    assert len(df) == 4
    assert df.loc[0, "spend"] == 1000000.0
    assert isinstance(df.loc[0, "spend"], float)
