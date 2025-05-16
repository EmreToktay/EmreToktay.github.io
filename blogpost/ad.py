import nbformat
from nbconvert import HTMLExporter
import os

# 1. Define paths
notebook_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\churn.ipynb"
output_html_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\churna.html"

# 2. Load notebook WITH outputs
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# 3. Configure HTML exporter to preserve everything
html_exporter = HTMLExporter()
html_exporter.exclude_input = False  # Keep code cells visible
html_exporter.exclude_output = False  # <- Critical: Ensures outputs are kept

# 4. Convert and save
html_data, _ = html_exporter.from_notebook_node(notebook)
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(html_data)

print(f"Successfully converted with outputs preserved: {output_html_path}")