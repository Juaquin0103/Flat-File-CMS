from flask import Flask, render_template, abort
import os

app = Flask(__name__)

CONTENT_DIR = "content"

@app.route('/')
def home():
    files = [f.replace('.md', '') for f in os.listdir(CONTENT_DIR)]
    return render_template('index.html', files=files)

@app.route('/<page_name>')
def render_page(page_name):
    path = os.path.join(CONTENT_DIR, f"{page_name}.md")
    
    if not os.path.exists(path):
        abort(404)
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    return render_template('page.html', content=content, title=page_name)

if __name__ == '__main__':
    app.run(debug=True)