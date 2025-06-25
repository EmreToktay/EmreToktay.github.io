from nbconvert.exporters import HTMLExporter
import nbformat

# 1. Dosya yolları
notebook_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\AB Sportsbook.ipynb"
output_html_path = r"C:\Users\Memre\Documents\GitHub\EmreToktay.github.io\blogpost\AB Sportsbooka.html"

# 2. Notebook'u yükle
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# 3. HTML Exporter ayarları
html_exporter = HTMLExporter()
html_exporter.exclude_input = False
html_exporter.exclude_output = False
html_exporter.template_name = 'classic'

# 4. Plotly JS
plotly_js = """
<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
</script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
"""

# 5. Mobil uyumlu CSS reset
responsive_css = """
<style>
/* Genel reset */
body, html {
    margin: 0;
    padding: 0;
    max-width: 100% !important;
    overflow-x: hidden !important;
    font-size: 16px;
}

/* Her türlü kutu için esneklik */
div, table, pre, code, blockquote, section, article, td, th {
    max-width: 100% !important;
    width: 100% !important;
    box-sizing: border-box;
    overflow-x: auto;
}

/* Kod blokları ve tablolar */
pre, code {
    white-space: pre-wrap !important;
    word-break: break-word;
}

/* Plotly container'ları */
.js-plotly-plot, .plotly-graph-div {
    max-width: 100% !important;
    height: auto !important;
}
</style>
"""

# 6. HTML çıktısı al
(body, resources) = html_exporter.from_notebook_node(notebook)

# 7. Hepsini <body>'nin sonuna ekle
final_inject = plotly_js + responsive_css
body = body.replace("</body>", f"{final_inject}</body>")

# 8. Dosyaya yaz
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(body)

print(f"✅ Mobil uyumlu HTML oluşturuldu: {output_html_path}")
