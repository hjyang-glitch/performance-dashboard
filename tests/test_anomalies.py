import pandas as pd
from anomalies import detect_anomalies


def test_detect_anomalies_flags_cpa_spike_with_creative_cause():
    df = pd.DataFrame([
        {"date": "2026-07-01", "channel": "Meta", "campaign": "캠페인A",
         "spend": 1000000, "conversions": 50, "revenue": 3000000,
         "creative_name": "발열스틱_영상_A_뷰티", "ctr": 0.031},
        {"date": "2026-07-02", "channel": "Meta", "campaign": "캠페인A",
         "spend": 1000000, "conversions": 20, "revenue": 1200000,
         "creative_name": "발열스틱_영상_A_뷰티", "ctr": 0.012},
    ])

    alerts = detect_anomalies(df, threshold=0.30)

    assert len(alerts) == 1
    alert = alerts[0]
    assert alert["channel"] == "Meta"
    assert alert["campaign"] == "캠페인A"
    assert alert["metric"] == "CPA"
    assert alert["pct_change"] > 0.30
    assert alert["likely_cause_creative"] == "발열스틱_영상_A_뷰티"
    assert alert["cause_ctr_drop_pct"] > 0.30


def test_detect_anomalies_ignores_stable_campaigns():
    df = pd.DataFrame([
        {"date": "2026-07-01", "channel": "Google", "campaign": "캠페인B",
         "spend": 500000, "conversions": 25, "revenue": 1500000,
         "creative_name": "소재B", "ctr": 0.02},
        {"date": "2026-07-02", "channel": "Google", "campaign": "캠페인B",
         "spend": 510000, "conversions": 24, "revenue": 1480000,
         "creative_name": "소재B", "ctr": 0.019},
    ])

    alerts = detect_anomalies(df, threshold=0.30)

    assert alerts == []
