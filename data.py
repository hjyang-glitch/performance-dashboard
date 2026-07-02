import gspread
import pandas as pd
import streamlit as st

SPREADSHEET_ID = "1hG8NLX0uv69CCUolP5u9Own-wZYXU_hWCRGCiWHwR9c"
WORKSHEET_NAME = "일별데이터"


def _get_client():
    creds = st.secrets["gcp_service_account"]
    return gspread.service_account_from_dict(creds)


def load_campaign_data() -> pd.DataFrame:
    client = _get_client()
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(WORKSHEET_NAME)
    records = sheet.get_all_records()
    df = pd.DataFrame(records)
    numeric_cols = ["spend", "conversions", "revenue", "ctr"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)
    return df
