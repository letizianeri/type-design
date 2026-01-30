import os
import re

folder_path = "/Users/a39339/Desktop/type design/PROGETTO FINALE/type-design/card-pages"

new_nav_content = (
'        <a href="../archivio.html#grid-archive" class="back-btn">&lt; INDIETRO</a>\n\n'
'        <div class="nav-right">\n'
'            <a href="../index.html">Intro</a>\n'
'            <a href="../archivio.html">Archivio</a>\n'
'            <a href="../specimen.html">Specimen</a>\n'
'            <a href="../about.html">About</a>\n'
'        </div>'
)

nav_pattern = re.compile(r"<nav[^>]*>.*?</nav>", re.DOTALL | re.IGNORECASE)

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        new_nav = f"<nav>\n{new_nav_content}\n</nav>"
        updated_content = nav_pattern.sub(new_nav, content)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"Aggiornato: {filename}")
