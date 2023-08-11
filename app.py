from flask import Flask

from routes.api import api
from routes.views import views

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)