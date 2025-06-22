# ⚾️ 야구 투수·타자 스탯 분석 프로젝트 (Baseball Stats Analysis)

---

## 🇰🇷 개요

* **목적**: Statiz에서 KBO 팀의 투수·타자 스탯을 크롤링하여, **승리(W)/패배(L)** 와 가장 강한 상관관계를 보이는 지표를 탐색합니다.
* **데이터 출처**: [Statiz](http://www.statiz.co.kr)
* **대상 시즌**: 2015년 \~ 2024년 (2025년은 진행 중이므로 제외)

## 🇰🇷 전처리 과정

1. **불필요 지표 제거**

   * 중복 혹은 내부용 컬럼: `정렬`, `R`, `rRA`, `rRA/9`, `RA9`, `CG`, `SHO`, `BK`, `WP`, `IB`, `WAR` 등
2. **연도 필터링**

   * 진행 중인 2025 시즌 데이터 제외
3. **타입 변환**

   * 누적 스탯(`G`, `IP`, `TBF`, `W`, `L`, `S`, `HD`, `ER`, `H`, `2B`, `3B`, `HR`, `BB`, `HP`, `SO`, `ROE`)을 `int`/`float`형으로 변환
4. **파생 변수 생성**

   * **장타(XBH)**: `2B + 3B + HR`
5. **비율 스탯 변환**

   * **경기당**: `S_per_game`, `HD_per_game`, `ER_per_game`, `H_per_game`, `BB_per_game`, `SO_per_game`, `XBH_per_game`
   * **9이닝당**: `ER_per_9IP`, `H_per_9IP`, `BB_per_9IP`, `SO_per_9IP`, `HR_per_9IP`, `XBH_per_9IP`
   * **타자당**: `SO_per_batter`, `BB_per_batter`, `H_per_batter`, `HR_per_batter`, `XBH_per_batter`

## 🇰🇷 분석 방법

1. **피어슨 상관계수 계산**: `W`, `L`과 모든 비율 지표 간 상관계수 산출
2. **히트맵 시각화**: 세로 형태 히트맵으로 각 지표와 `W`/`L` 관계 표시
3. **산점도 시각화**: `plot_all_scatter.py`를 통해 모든 비율 지표 vs `W`/`L` 산점도 자동 생성
4. **몽타주 생성**: 18장(승리 vs)/18장(패배 vs) 산점도를 3×6 그리드 이미지로 병합

## 🇰🇷 주요 인사이트

* **승리(W)**: 높은 세이브·탈삼진 비율, 낮은 볼넷·자책점 비율이 양(+) 상관
* **패배(L)**: 높은 자책점·피안타·볼넷 비율이 양(+) 상관

## 🇬🇧 Overview

* **Goal**: Identify features from KBO team pitching/hitting stats most correlated with Wins (W) and Losses (L).
* **Source**: Statiz ([http://www.statiz.co.kr](http://www.statiz.co.kr))
* **Seasons**: 2015–2024 (exclude ongoing 2025 data)

### Preprocessing

1. **Drop Unnecessary Columns**: remove internal/dup columns (`WAR`, `RA9`, etc.)
2. **Year Filtering**: exclude 2025 ongoing season
3. **Type Conversion**: convert cumulative stats to numeric
4. **Derived Features**: `XBH = 2B + 3B + HR`
5. **Rate Stats**: per\_game, per\_9IP, per\_batter for selected indicators

### Analysis

* **Correlation**: Pearson r between W/L and rate stats
* **Heatmaps**: vertical heatmaps with annotated r values
* **Scatter Plots**: auto-generate for all rate stats vs W/L
* **Montage**: combine scatter plots into grid images

### Key Insights

* **Wins**: positively correlated with Saves, K-rates; negatively with BB/ER rates
* **Losses**: positively correlated with ER, Hits, BB rates

## Requirements

* Python 3.8+
* `pandas`, `requests`, `beautifulsoup4`, `matplotlib`, `Pillow`

---

*By 규태*
