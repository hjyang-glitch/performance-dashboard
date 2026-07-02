import pandas as pd


def detect_anomalies(df: pd.DataFrame, threshold: float = 0.30) -> list[dict]:
    alerts = []
    df = df.sort_values("date")

    for (channel, campaign), group in df.groupby(["channel", "campaign"]):
        if len(group) < 2:
            continue

        yesterday, today = group.iloc[-2], group.iloc[-1]

        cpa_yesterday = _safe_div(yesterday["spend"], yesterday["conversions"])
        cpa_today = _safe_div(today["spend"], today["conversions"])
        if cpa_yesterday is None or cpa_today is None:
            continue

        pct_change = _safe_div(cpa_today - cpa_yesterday, cpa_yesterday)
        if pct_change is None or abs(pct_change) < threshold:
            continue

        ctr_drop_pct = None
        if yesterday["ctr"] and yesterday["ctr"] != 0:
            ctr_drop_pct = (yesterday["ctr"] - today["ctr"]) / yesterday["ctr"]

        alerts.append({
            "channel": channel,
            "campaign": campaign,
            "metric": "CPA",
            "pct_change": pct_change,
            "today_value": cpa_today,
            "yesterday_value": cpa_yesterday,
            "likely_cause_creative": today["creative_name"],
            "cause_ctr_drop_pct": ctr_drop_pct,
        })

    return alerts


def _safe_div(numerator, denominator):
    if denominator in (0, None) or pd.isna(denominator):
        return None
    return numerator / denominator
