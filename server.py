import os

from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = 'abc'

@app.route('/')
def tech_stack_render():
    return render_template('tech_stack.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)