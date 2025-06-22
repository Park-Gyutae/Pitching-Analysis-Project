import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 저장 디렉토리 경로
os.makedirs("data/raw", exist_ok=True)
raw_csv_path = "data/raw/pitching_stats.csv"
raw_pkl_path = "data/raw/pitching_stats.pkl"

# 1) 크롤링할 URL 설정
url = (
    'https://statiz.sporki.com/stats/'
    '?m=team&m2=pitching&m3=default'
    '&so=WAR&ob=DESC'
    '&year=2025&sy=2005&ey=2024'
    '&...'
    '&pr=200'  # 페이지당 표시할 행 수 (100개면 pr=100)
)

# 2) HTTP GET 요청 (User-Agent 설정 권장)
response = requests.get(url)
html = response.text

# 3) BeautifulSoup 으로 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 4) 두 번째 <table> 태그를 선택 (0은 요약, 1이 팀별 상세 통계)
temp = soup.find_all("table")[1]

# 5) 컬럼명을 미리 정의
columns = [
    "Rank", "Team", "Year", "정렬",
    "G", "GS", "GR", "GF", "CG", "SHO",
    "W", "L", "S", "HD", "IP", "ER",
    "R", "rRA", "TBF", "H", "2B", "3B",
    "HR", "BB", "HP", "IB", "SO", "ROE",
    "BK", "WP", "ERA", "RA9", "rRA9",
    "FIP", "WHIP", "WAR"
]

# 6) 빈 DataFrame 생성 (최대 182개 예상)
df = pd.DataFrame(index=range(182), columns=columns)

# 7) 테이블의 모든 <tr> 태그 리스트화
rows = temp.find_all("tr")

# 8) 실제 데이터 채우기 위한 카운터
l = 0

# 9) 테이블 헤더(0), 요약(1) 다음부터 반복
for tr in rows[2:]:
    tds = tr.find_all("td")

    # 10) td 태그가 36개인 경우만 순위별 데이터로 간주
    if len(tds) == 36:
        # 11) 한 행의 모든 셀(Text) 값을 리스트로 추출해 한 번에 할당
        df.loc[l, :] = [td.get_text(strip=True) for td in tds]
        l += 1

# 12) 실제 채워진 만큼만 잘라내고 인덱스 초기화
df = df.iloc[:l].reset_index(drop=True)

# CSV로 저장 (한글 깨짐 방지)
df.to_csv(raw_csv_path, index=False, encoding="utf-8-sig")
# Pickle로 저장
df.to_pickle(raw_pkl_path)

print(f"✅ Raw data saved to:\n  CSV → {raw_csv_path}\n  PKL → {raw_pkl_path}")