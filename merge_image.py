from PIL import Image
import os

# 18장씩 한 장으로 합치는 몽타주 스크립트

def make_montage(image_paths, montage_path,
                 rows, cols, thumb_size=(400, 300), padding=5, bg_color=(255,255,255)):
    w, h = thumb_size
    montage_w = cols * w + (cols + 1) * padding
    montage_h = rows * h + (rows + 1) * padding

    montage = Image.new("RGB", (montage_w, montage_h), bg_color)
    for idx, img_path in enumerate(image_paths):
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"File not found: {img_path}")
        img = Image.open(img_path).convert("RGB")
        img = img.resize(thumb_size, Image.LANCZOS)

        row = idx // cols
        col = idx % cols
        x = padding + col * (w + padding)
        y = padding + row * (h + padding)
        montage.paste(img, (x, y))

    montage.save(montage_path)
    print(f"✅ Montage saved to {montage_path}")

if __name__ == '__main__':
    image_dir = 'figures/all_scatter'
    all_files = sorted([f for f in os.listdir(image_dir) if f.lower().endswith('.png')])

    # W_로 시작하는 18장
    w_files = [os.path.join(image_dir, f) for f in all_files if f.startswith('W_vs_')]
    # L_로 시작하는 18장
    l_files = [os.path.join(image_dir, f) for f in all_files if f.startswith('L_vs_')]

    os.makedirs('figures', exist_ok=True)

    # 승리: 3행×6열 = 18장
    make_montage(
        image_paths=w_files,
        montage_path='figures/W_scatter_montage.png',
        rows=3, cols=6
    )

    # 패배: 3행×6열 = 18장
    make_montage(
        image_paths=l_files,
        montage_path='figures/L_scatter_montage.png',
        rows=3, cols=6
    )
