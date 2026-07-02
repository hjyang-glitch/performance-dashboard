import streamlit as st

from anomalies import detect_anomalies
from data import load_campaign_data

st.set_page_config(page_title="퍼포먼스 대시보드", layout="wide")
st.title("퍼포먼스 대시보드")

tab_alerts, tab_channel, tab_creative, tab_ab, tab_pacing = st.tabs(
    ["🔴 오늘의 알림", "채널 성과", "소재 성과", "AB테스트", "예산 페이싱"]
)

with tab_alerts:
    df = load_campaign_data()
    alerts = detect_anomalies(df)

    if not alerts:
        st.success("이상치 없음 — 전일 대비 급변한 캠페인이 없습니다.")
    for alert in alerts:
        direction = "+" if alert["pct_change"] > 0 else ""
        cause_line = ""
        if alert["cause_ctr_drop_pct"] and alert["cause_ctr_drop_pct"] > 0:
            cause_line = (
                f"  \n└ 원인 추정: 소재 \"{alert['likely_cause_creative']}\" "
                f"CTR {alert['cause_ctr_drop_pct']*100:.0f}% 하락"
            )
        st.warning(
            f"**{alert['channel']} - {alert['campaign']}**  \n"
            f"{alert['metric']} {alert['today_value']:,.0f}원 "
            f"({direction}{alert['pct_change']*100:.0f}% vs 어제)"
            + cause_line
        )

with tab_channel:
    st.info("채널 성과 탭 — 후속 플랜에서 구현 예정")

with tab_creative:
    st.info("소재 성과 탭 — 후속 플랜에서 구현 예정")

with tab_ab:
    st.info("AB테스트 탭 — 후속 플랜에서 구현 예정")

with tab_pacing:
    st.info("예산 페이싱 탭 — 후속 플랜에서 구현 예정")
