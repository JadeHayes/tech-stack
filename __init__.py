"""
The Flask application that handles the API calls from our on-boarding
react application
"""
from flask import Flask


from werkzeug.contrib.fixers import ProxyFix
from .routes.tech_stack import tech_stack_blueprint

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = 'abc'

app.register_blueprint(tech_stack_blueprint, url_prefix='/tech-stack')
