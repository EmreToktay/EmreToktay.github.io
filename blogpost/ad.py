import nbformat
from nbconvert import HTMLExporter
import os

# 1. Define ABSOLUTE paths
notebook_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\fraud.ipynb"
output_html_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\frauda.html"

# 2. Load the notebook WITHOUT executing it
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# 3. Convert to HTML (preserve existing outputs)
html_exporter = HTMLExporter()
html_exporter.exclude_input = False  # Set to True to hide code cells
html_data, _ = html_exporter.from_notebook_node(notebook)

# 4. Save the HTML file
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_data)

print(f"Successfully converted '{notebook_path}' to '{output_html_path}'")