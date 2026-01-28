import re

file_path = "/Users/a39339/Desktop/type design/PROGETTO FINALE/type-design/archivio.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(
    r'<a\s+href="#"[^>]*>\s*<img\s+src="([^"]*Card-(\d{2})\.png)"[^>]*>\s*</a>'
)

def replace_href(match):
    img_src = match.group(1)
    num = match.group(2)
    return f'<a href="./card-pages/card-{num}.html"><img src="{img_src}"></a>'

new_html = pattern.sub(replace_href, html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_html)

print("Sostituzione completata ✅")
