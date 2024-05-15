from flask import Flask


app = Flask(__name__, template_folder="../../ui/templates", static_folder="../../ui/static")
app.config['SECRET_KEY'] = '1234'

from infra import routes