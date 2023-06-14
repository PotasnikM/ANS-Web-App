from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.debug = True
app.config["CACHE_TYPE"] = "SimpleCache"
cache = Cache(app)

from web_app import routes