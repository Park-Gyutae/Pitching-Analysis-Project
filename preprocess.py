import os
import pandas as pd

# 저장 디렉토리 생성
os.makedirs("data/processed", exist_ok=True)


def load_raw(path: str) -> pd.DataFrame:
    """원시 Pickle 파일을 읽어 DataFrame으로 반환합니다."""
    return pd.read_pickle(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    전처리 단계:
    1) 불필요 컬럼 제거 (Year 포함)
    2) 숫자형 변환 및 XBH(장타) 생성
    3) 비율 스탯을 만들 지표를 세 축으로 나누어 계산:
       - 경기당(per_game)
       - 9이닝당(per_9IP)
       - 타자당(per_batter)
    4) 최종 DataFrame 구성 (Year 제외)
    """
    # 1) 드롭 대상 컬럼
    drop_cols = [
        'Year', '정렬', 'R', 'rRA', 'rRA/9', 'RA9',
        'CG', 'SHO', 'BK', 'WP', 'IB', 'WAR',
        'GS', 'GR', 'GF'
    ]
    df = df.drop(columns=drop_cols, errors='ignore')

    # 2) 숫자형 변환 대상
    base_cols = ['G', 'IP', 'TBF']
    raw_cols  = ['W', 'L', 'S', 'HD', 'ER', 'H', '2B', '3B', 'HR', 'BB', 'HP', 'SO', 'ROE']
    df[base_cols + raw_cols] = df[base_cols + raw_cols].apply(pd.to_numeric, errors='coerce')

    # XBH: 장타(2루타 + 3루타 + 홈런)
    df['XBH'] = df[['2B', '3B', 'HR']].sum(axis=1)

    # 3) 축별 지표 그룹 정의
    per_game_cols   = ['S', 'HD', 'ER', 'H', 'BB', 'SO', 'XBH']
    per_9IP_cols    = ['ER', 'H', 'BB', 'SO', 'HR', 'XBH']
    per_batter_cols = ['SO', 'BB', 'H', 'HR', 'XBH']  # TBF 대비

    # 4) 비율 스탯 계산
    per_game   = df[per_game_cols].div(df['G'], axis=0).add_suffix('_per_game')
    per_9ip    = df[per_9IP_cols].mul(9).div(df['IP'], axis=0).add_suffix('_per_9IP')
    per_batter = df[per_batter_cols].div(df['TBF'], axis=0).add_suffix('_per_batter')

    # 5) 최종 DataFrame 구성 (Year 제외)
    df_final = pd.concat([
        df[['Team', 'W', 'L']],
        per_game, per_9ip, per_batter
    ], axis=1)
    return df_final


def save_processed(df: pd.DataFrame, csv_path: str, pkl_path: str):
    """전처리된 DataFrame을 CSV와 Pickle 형식으로 저장합니다."""
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    df.to_pickle(pkl_path)


if __name__ == '__main__':
    raw_pkl            = 'data/raw/pitching_stats.pkl'
    processed_csv_path = 'data/processed/pitching_stats_clean.csv'
    processed_pkl_path = 'data/processed/pitching_stats_clean.pkl'

    df_raw   = load_raw(raw_pkl)
    df_clean = clean_data(df_raw)
    save_processed(df_clean, processed_csv_path, processed_pkl_path)

    print(f"✅ 전처리 완료: {df_clean.shape[0]} rows, {df_clean.shape[1]} cols")
