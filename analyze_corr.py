import os
import pandas as pd
import matplotlib.pyplot as plt

# 분석 스크립트: 승/패와 다른 지표들 간 상관계수 계산 및 히트맵 생성

def main():
    # 1) 전처리된 데이터 로드
    df = pd.read_csv("data/processed/pitching_stats_clean.csv", encoding="utf-8-sig")

    # 2) 숫자형 칼럼 추출
    num_df = df.select_dtypes(include="number")

    # 3) 피어슨 상관계수 계산
    corr_matrix = num_df.corr(method="pearson")

    # 4) W 및 L 컬럼과 상관계수 추출 (모든 지표), 상관계수 내림차순 정렬
    corr_w = corr_matrix["W"].drop("W").sort_values(ascending=False)
    corr_l = corr_matrix["L"].drop("L").sort_values(ascending=False)

    # 5) 히트맵 디렉토리 생성) 히트맵 디렉토리 생성
    out_dir = "figures/heatmaps"
    os.makedirs(out_dir, exist_ok=True)

    # 6) 히트맵 생성 함수 (annot=True)
    def plot_vertical_heatmap(series, title, filename):
        # series를 DataFrame으로 변환(한 열)
        df_hm = pd.DataFrame(series)
        fig, ax = plt.subplots(figsize=(2, len(df_hm)*0.4), dpi=100)
        im = ax.imshow(df_hm.values, aspect='auto', cmap='coolwarm', vmin=-1, vmax=1)
        # 축 설정
        ax.set_yticks(range(len(df_hm.index)))
        ax.set_yticklabels(df_hm.index, fontsize=8)
        ax.set_xticks([0])
        ax.set_xticklabels([title], fontsize=10)
        # 셀별 상관계수 텍스트 표시
        for i, val in enumerate(df_hm[title]):
            ax.text(0, i, f"{val:.2f}", ha='center', va='center', color='black', fontsize=8)
        # 컬러바
        cbar = fig.colorbar(im, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
        cbar.set_label('Pearson r', fontsize=8)
        ax.set_title(f"Correlation with {title}", fontsize=12)
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, filename))
        plt.close(fig)
        print(f"Saved heatmap: {filename}")

    # 7) 승리 W 히트맵 저장
    plot_vertical_heatmap(corr_w.rename('W'), 'W', 'heatmap_W_all.png')
    # 8) 패배 L 히트맵 저장
    plot_vertical_heatmap(corr_l.rename('L'), 'L', 'heatmap_L_all.png')

    print(f"✅ All heatmaps saved in {out_dir}")

if __name__ == "__main__":
    main()
