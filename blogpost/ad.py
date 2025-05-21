from nbconvert.exporters import HTMLExporter
import nbformat
import os

# 1. Define paths
notebook_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\bonus_request.ipynb"
output_html_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\bonus_requesta.html"

# 2. Load notebook WITH outputs
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# 3. Configure HTML exporter with Plotly support
html_exporter = HTMLExporter()
html_exporter.exclude_input = False  # Keep code cells visible
html_exporter.exclude_output = False  # Ensures outputs are kept

# Add these configurations for Plotly
html_exporter.template_name = 'classic'
html_exporter.extra_template_paths = ['.']
html_exporter.config.TemplateExporter.extra_template_basedirs = ['.'] 

# Add Plotly JS requirement (critical fix)
plotly_js = """
<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
</script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
"""
html_exporter.template_data = {
    'plotly_js': plotly_js
}

# 4. Convert and save
(body, resources) = html_exporter.from_notebook_node(notebook)

# Inject Plotly JS at the end of body if not already present
if "plotly-latest.min.js" not in body:
    body = body.replace("</body>", f"{plotly_js}</body>")

with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(body)

print(f"Successfully converted with outputs preserved: {output_html_path}")