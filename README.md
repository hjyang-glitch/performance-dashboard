# 퍼포먼스 대시보드

퍼포먼스 마케팅팀 일일 확인용 Streamlit 대시보드.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

`.streamlit/secrets.toml`에 `gcp_service_account` 블록이 필요합니다 (Google Cloud 서비스 계정 JSON).
저장소는 public이므로 이 파일은 절대 커밋하지 마세요 (`.gitignore`에 이미 포함됨).

## 데이터 소스

Google Sheet "퍼포먼스 대시보드 - 캠페인 일별 데이터" (`일별데이터` 탭)를 읽습니다.
스프레드시트를 서비스 계정 이메일과 공유(Viewer 권한)해야 앱이 데이터를 읽을 수 있습니다.

## 현재 범위

- 🔴 오늘의 알림 탭만 실제 구현됨 (전일 대비 CPA ±30% 이상 급변 시 알림, 원인 소재 CTR 하락 함께 표시)
- 채널 성과 / 소재 성과 / AB테스트 / 예산 페이싱 탭은 후속 플랜에서 구현 예정
