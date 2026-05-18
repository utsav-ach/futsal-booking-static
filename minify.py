import htmlmin
import os

input_file = 'index.html'
output_file = 'index.html'

with open(input_file, 'r', encoding='utf-8') as f:
    original_html = f.read()

minified_html = htmlmin.minify(
    original_html,
    remove_comments=True,
    remove_empty_space=True
)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(minified_html)

original_size = len(original_html.encode('utf-8'))
minified_size = len(minified_html.encode('utf-8'))
saved = original_size - minified_size
percent = round((saved / original_size) * 100, 2)

print(f"Original size  : {original_size} bytes")
print(f"Minified size  : {minified_size} bytes")
print(f"Saved          : {saved} bytes ({percent}% reduction)")
print("Minification complete!")
