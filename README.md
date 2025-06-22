# Pitching Stats Analyzing Project

2025-1학기 연세대학교 수학과 ‘수학과 프로그래밍’ 기말 프로젝트입니다.  
파이썬의 pandas, matplotlib을 활용하여 KBO 팀 투수 스탯과 경기 승·패 간의 상관관계를 다각도로 분석합니다.

---

## 목차
1. [프로젝트 개요](#프로젝트-개요)  
2. [프로젝트 동기](#프로젝트-동기)  
3. [실행 방법](#실행-방법)  
   - [1. 데이터 크롤링](#1-데이터-크롤링)  
   - [2. 데이터 전처리](#2-데이터-전처리)  
   - [3. 산점도 자동 생성](#3-산점도-자동-생성)  
   - [4. 상관계수 히트맵](#4-상관계수-히트맵)  
   - [5. 이미지 몽타주](#5-이미지-몽타주)  
4. [분석 결과](#분석-결과)  
5. [결론](#결론)  
6. [Requirements](#requirements)  

---

## 프로젝트 개요

- **분석 대상**: 2005~2024년 KBO리그 팀 투수 통계
- **목표**:
  1. 누적 스탯을 ‘경기당’, ‘9이닝당’, ‘타자당’ 비율 스탯으로 변환  
  2. ‘승리(W)’·‘패배(L)’와 각 비율 스탯 간 피어슨 상관계수 산출  
  3. 히트맵 및 산점도 시각화를 통해 핵심 투수 스탯 도출  
- **사용 기술**: `Python, pandas, BeautifulSoup, matplotlib, Pillow`

## 프로젝트 계획 동기

---

## 목차
1. [프로젝트 개요](#프로젝트-개요)  
2. [프로젝트 동기](#프로젝트-동기)  
3. [실행 방법](#실행-방법)  
   - [1. 데이터 크롤링](#1-데이터-크롤링)  
   - [2. 데이터 전처리](#2-데이터-전처리)  
   - [3. 산점도 자동 생성](#3-산점도-자동-생성)  
   - [4. 상관계수 히트맵](#4-상관계수-히트맵)  
   - [5. 이미지 몽타주](#5-이미지-몽타주)  
4. [분석 결과](#분석-결과)  
5. [결론](#결론)  
6. [Requirements](#requirements)  

---

## 프로젝트 개요
- **분석 대상**: 2005~2024년 KBO 리그 팀 투수 통계  
- **목표**:  
  1. 누적 스탯을 ‘경기당’, ‘9이닝당’, ‘타자당’ 비율 스탯으로 변환  
  2. ‘승리(W)’·‘패배(L)’와 각 비율 스탯 간 피어슨 상관계수 산출  
  3. 히트맵·산점도 시각화를 통해 핵심 투수 스탯 도출  
- **사용 기술**: Python, pandas, BeautifulSoup, matplotlib, Pillow  

---

## 프로젝트 동기
어린 시절부터 야구와 특히 투수의 **투구 스타일**에 관심이 많았습니다.  
경험적 감각 대신 **객관적 데이터**로 “어떤 지표가 승·패에 가장 큰 영향을 미치는지” 밝히고자 본 프로젝트를 시작했습니다.  
이를 통해 팀 운영 전략에 활용할 수 있는 인사이트를 제시하고, 데이터 기반 의사결정 과정을 경험합니다.

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

### 산점도 몽타주

* 승리 대비 산점도

![승리 대비 산점도](https://raw.githubusercontent.com/Park-Gyutae/Pitching-Analysis-Project/main/figures/W_scatter_montage.png)  

* 패배 대비 산점도

![패배 대비 산점도](https://raw.githubusercontent.com/Park-Gyutae/Pitching-Analysis-Project/main/figures/L_scatter_montage.png)

### 피어슨 상관계수 히트맵

| ![승리 히트맵](https://raw.githubusercontent.com/Park-Gyutae/Pitching-Analysis-Project/main/figures/heatmaps/heatmap_W_all.png) | ![패배 히트맵](https://raw.githubusercontent.com/Park-Gyutae/Pitching-Analysis-Project/main/figures/heatmaps/heatmap_L_all.png) |

| 승리(`W`)와 지표 간 상관 | 패배(`L`)와 지표 간 상관 |

### 요약

#### 승리(`W`)와 지표 간 상관

* **강한 양의 상관** (r ≥ +0.40)

    * `S_per_game`, `SO_per_batter`, `HD_per_game`

* **중간 정도 양의 상관** (+0.30 ≤ r < +0.40)

    * `SO_per_game`, `SO_per_9IP`

* **거의 상관 없음** (|r| < 0.10)

    * `XBH_per_batter`, `HR_per_batter`, `XBH_per_game`, `HR_per_9IP`

* **강한 음의 상관** (r ≤ –0.40)

    * `BB_per_9IP (–0.48)`, `BB_per_game (–0.46)`, `BB_per_batter (–0.44)`, `ER_per_9IP (–0.41)`, `ER_per_game (–0.39)`

#### 패배(`L`)와 지표 간 상관

* **매우 강한 양의 상관** (r ≥ +0.60)

    * `ER_per_game`, `ER_per_9IP`

* **매우 강한 양의 상관** (r ≥ +0.60)

    * `H_per_9IP`, `H_per_game`, `H_per_batter`, `BB_per_9IP`

* **거의 상관 없음** (|r| < 0.10)

    * `SO_per_9IP`, `SO_per_game`, `SO_per_batter`

* **강한 음의 상관** (r ≤ –0.60)

    * `S_per_game`, `W`

## 결론

- **승리 예측 핵심 요인**  
  - **양의 상관**  
    - 세이브 경기 비율 (`S_per_game`)  
    - 타자당 탈삼진 비율 (`SO_per_batter`)  
    - 홀드 경기 비율 (`HD_per_game`)  
  - **음의 상관**  
    - 볼넷 비율 전반 (`BB_per_game`, `BB_per_9IP`, `BB_per_batter`)  
    - 자책점 비율 (`ER_per_game`, `ER_per_9IP`)  

- **패배 예측 핵심 요인**  
  - **양의 상관**  
    - 자책점 비율 전반 (`ER_per_game`, `ER_per_9IP`)  
    - 피안타 비율 전반 (`H_per_game`, `H_per_9IP`, `H_per_batter`)  
  - **음의 상관**  
    - 세이브 경기 비율 (`S_per_game`)  
    - 승리 수 (`W`)  

- **예측력 낮은 지표**  
  - 사구, 장타, 탈삼진 전반, 실책출루  
  (`HP_per_*`, `XBH_per_*`, `SO_per_*`, `ROE`) 등은  
  상관계수가 거의 0에 가까워 승패 예측에 크게 기여하지 않음

> **시사점**  
> - **불펜 성과 강화** (세이브·홀드·탈삼진)  
> - **제구력 개선** (볼넷·자책점·피안타 최소화)  
>  
> 위 두 가지 전략이 팀의 승리 확률을 최고조로 끌어올리고, 패배 요인을 효과적으로 억제할 수 있습니다.
> 홈런, 장타, 탈삼진, 실책 등이 승패 예측에 크게 기여하지 않는다는 사실도 놀라웠습니다.

## Requirements

Python 3.8+

pandas, requests, beautifulsoup4, matplotlib, Pillow