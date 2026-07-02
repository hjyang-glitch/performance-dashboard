import pandas as pd
from data import load_campaign_data
import data as data_module


def test_load_campaign_data_returns_typed_dataframe(monkeypatch):
    fake_records = [
        {
            "date": "2026-07-01", "channel": "Meta", "campaign": "캠페인A",
            "spend": "1000000", "conversions": "50", "revenue": "3000000",
            "creative_name": "발열스틱_영상_A_뷰티", "ctr": "0.031",
        },
    ]

    class FakeWorksheet:
        def get_all_records(self):
            return fake_records

    class FakeSpreadsheet:
        def worksheet(self, name):
            return FakeWorksheet()

    class FakeClient:
        def open_by_key(self, key):
            return FakeSpreadsheet()

    monkeypatch.setattr(data_module, "_get_client", lambda: FakeClient())

    df = load_campaign_data()

    assert list(df.columns) == [
        "date", "channel", "campaign", "spend", "conversions",
        "revenue", "creative_name", "ctr",
    ]
    assert df.loc[0, "spend"] == 1000000.0
    assert isinstance(df.loc[0, "spend"], float)
