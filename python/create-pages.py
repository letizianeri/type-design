from pathlib import Path

# percorso
folder = Path("/Users/a39339/Desktop/type design/PROGETTO FINALE/type-design/card-pages")

# crea i file
for i in range(1, 25):
    filename = f"card-{i:02}.html"
    file_path = folder / filename
    file_path.touch(exist_ok=True)
