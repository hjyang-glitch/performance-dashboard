import pandas as pd

# 임시 샘플 데이터. 채널+앱스플라이어 조인 파이프라인이 완성되면
# 이 함수 내부만 실제 데이터 소스(시트/BigQuery 등) 조회로 교체하면 된다.
_SAMPLE_RECORDS = [
    {"date": "2026-07-01", "channel": "Meta", "campaign": "캠페인A",
     "spend": 1000000, "conversions": 50, "revenue": 3000000,
     "creative_name": "발열스틱_영상_A_뷰티", "ctr": 0.031},
    {"date": "2026-07-02", "channel": "Meta", "campaign": "캠페인A",
     "spend": 1000000, "conversions": 20, "revenue": 1200000,
     "creative_name": "발열스틱_영상_A_뷰티", "ctr": 0.012},
    {"date": "2026-07-01", "channel": "Google", "campaign": "캠페인B",
     "spend": 500000, "conversions": 25, "revenue": 1500000,
     "creative_name": "소재B", "ctr": 0.02},
    {"date": "2026-07-02", "channel": "Google", "campaign": "캠페인B",
     "spend": 510000, "conversions": 24, "revenue": 1480000,
     "creative_name": "소재B", "ctr": 0.019},
]


def load_campaign_data() -> pd.DataFrame:
    df = pd.DataFrame(_SAMPLE_RECORDS)
    numeric_cols = ["spend", "conversions", "revenue", "ctr"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)
    return df
