# Pitching Stats Analyzing Project

2025-1학기 연세대학교 수학과 ‘수학과 프로그래밍’ 기말 프로젝트입니다.  
파이썬의 pandas, matplotlib을 활용하여 KBO 팀 투수 스탯과 경기 승·패 간의 상관관계를 다각도로 분석합니다.

## 프로젝트 개요

- **분석 대상**: 2005~2024년 KBO리그 팀 투수 통계
- **목표**:
  1. 누적 스탯을 ‘경기당’, ‘9이닝당’, ‘타자당’ 비율 스탯으로 변환  
  2. ‘승리(W)’·‘패배(L)’와 각 비율 스탯 간 피어슨 상관계수 산출  
  3. 히트맵 및 산점도 시각화를 통해 핵심 투수 스탯 도출  
- **사용 기술**: `Python, pandas, BeautifulSoup, matplotlib, Pillow`

## 프로젝트 계획 동기

저는 어릴 때부터 야구를 즐겨 보며, 특히 투수의 **투구 스타일**과 **기술 지표**가 경기 결과에 어떤 영향을 미치는지 늘 궁금했습니다.  
수학적·프로그래밍 기법을 통해 실제 KBO 통계 데이터를 분석하면,  
- 경험적 감각에만 의존하지 않고  
- 객관적인 수치로 승·패 요인을 파악할 수 있을 것이라 생각했습니다. 

이를 통해  
1. 팀 운영 전략에 활용할 수 있는 “승리·패배 예측 인사이트”를 제시하고  
2. 데이터 기반 의사결정(Data-Driven Decision Making)을 경험해 보고자 본 프로젝트를 기획하게 되었습니다.

## 실행 방법

### 1. 데이터 크롤링

Statiz 웹사이트에서 투수 통계 데이터를 가져와 data/raw/에 저장합니다.

> ```python statiz_crawler.py```

### 2. 데이터 전처리

raw Pickle 파일을 읽어 불필요 column을 제거하고,
`피안타`, `피홈런` 등의 **누적 스탯**을 `경기당`, `9이닝당`, `타자당`의 **비율 스탯**으로 변환한 뒤 `data/processed`/에 저장합니다.

> ```python preprocess.py```

### 3. 산점도 자동 생성

승·패와 모든 비율 지표 간 산점도를 `figures/all_scatter/` 폴더에 출력합니다.

> ```python scripts/plot_all_scatter.py```

### 4. 상관계수 히트맵

피어슨 상관계수를 계산하고, ```figures/heatmaps/```에 세로 히트맵을 저장합니다.

> ```python scripts/analyze_corr.py```

### 5. 이미지 몽타주
생성된 산점도 18장씩을 각각 한 장의 몽타주 이미지로 합쳐 figures/에 저장합니다.

> ```python merge_images.py```

## 분석 결과

![승리 대비 산점도](https://github.com/Park-Gyutae/Pitching-Analysis-Project/blob/main/figures/W_scatter_montage.png)

![패배 대비 산점도](https://github.com/Park-Gyutae/Pitching-Analysis-Project/blob/main/figures/L_scatter_montage.png)

![승리 피어슨 상관계수 히트맵](https://github.com/Park-Gyutae/Pitching-Analysis-Project/blob/main/figures/heatmaps/heatmap_W_all.png)

![승리 피어슨 상관계수 히트맵](https://github.com/Park-Gyutae/Pitching-Analysis-Project/blob/main/figures/heatmaps/heatmap_L_all.png)
