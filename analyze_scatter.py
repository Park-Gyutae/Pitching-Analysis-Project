import os
import pandas as pd
import matplotlib.pyplot as plt

def make_scatter_plots(df, out_dir="figures/all_scatter"):
    """
    df: 전처리된 DataFrame (숫자형 지표 + W, L 컬럼 포함)
    out_dir: 이미지가 저장될 디렉토리
    """
    os.makedirs(out_dir, exist_ok=True)

    # 1) 숫자형 컬럼 리스트 (W, L 제외)
    num_cols = df.select_dtypes(include="number").columns.drop(["W", "L"])

    # 2) 각 지표에 대해 W vs col, L vs col 산점도 저장
    for col in num_cols:
        # 승리 vs 지표
        plt.figure(figsize=(6, 4), dpi=100)
        plt.scatter(df[col], df["W"], s=20, alpha=0.6)
        plt.xlabel(col)
        plt.ylabel("W")
        plt.title(f"W vs {col}")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{out_dir}/W_vs_{col}.png")
        plt.close()

        # 패배 vs 지표
        plt.figure(figsize=(6, 4), dpi=100)
        plt.scatter(df[col], df["L"], s=20, alpha=0.6, color="C1")
        plt.xlabel(col)
        plt.ylabel("L")
        plt.title(f"L vs {col}")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{out_dir}/L_vs_{col}.png")
        plt.close()

    print(f"✅ 완료: {len(num_cols)*2}장의 산점도가 '{out_dir}' 에 저장되었습니다.")

if __name__ == "__main__":
    # 1) 전처리된 데이터 로드
    df = pd.read_csv("data/processed/pitching_stats_clean.csv", encoding="utf-8-sig")

    # 2) 산점도 생성
    make_scatter_plots(df)
