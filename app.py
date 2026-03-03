from flask import Flask, render_template, abort
import os
import markdown

app = Flask(__name__)

# Configuración de rutas
CONTENT_DIR = "content"

def get_html_from_md(file_name):
    path = os.path.join(CONTENT_DIR, f"{file_name}.md")
    if not os.path.exists(path):
        return None
    
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        # Aquí ocurre la "magia": convertimos Markdown a HTML puro
        return markdown.markdown(text)

@app.route('/')
def index():
    # Escaneamos la carpeta para generar un índice automático
    files = [f.replace('.md', '') for f in os.listdir(CONTENT_DIR) if f.endswith('.md')]
    return render_template('index.html', files=files)

@app.route('/<page>')
def render_page(page):
    content_html = get_html_from_md(page)
    if content_html is None:
        abort(404)
    return render_template('page.html', content=content_html, title=page)

if __name__ == '__main__':
    app.run(debug=True)