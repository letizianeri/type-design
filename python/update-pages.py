import os
import re

BASE_DIR = "/Users/a39339/Desktop/type design/PROGETTO FINALE/type-design/card-pages"

for i in range(1, 25):
    num = f"{i:02d}"
    filename = f"card-{num}.html"
    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filepath):
        print(f"⚠️ File non trovato: {filename}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()


    # img nella left-col
    html = re.sub(
        r'(<div class="left-col">[\s\S]*?<img)[^>]*(>)',
        r'\1\2',
        html,
        count=1
    )

    # img nella bottom-row
    html = re.sub(
        r'(<div class="bottom-row">[\s\S]*?<img)[^>]*(>)',
        r'\1\2',
        html,
        count=1
    )

    card_img = f'../assets/immagini/archivio/cards/Card-{num}.png'
    invito_img = f'../assets/immagini/archivio/inviti/invito_{num}.png'

    # left-col
    html = re.sub(
        r'(<div class="left-col">[\s\S]*?<img)(>)',
        rf'\1 src="{card_img}" class="card-img"\2',
        html,
        count=1
    )

    # bottom-row
    html = re.sub(
        r'(<div class="bottom-row">[\s\S]*?<img)(>)',
        rf'\1 src="{invito_img}" class="invito-img"\2',
        html,
        count=1
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Ripulito e aggiornato {filename}")
