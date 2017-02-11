from flask import Flask, request, render_template, url_for
from test.urls import urls

app = Flask(__name__)
app.secret_key = "mockapi.dev"
from flask_cors  import CORS, cross_origin
CORS(app)
# app.debug = True

for url in urls:
    app.add_url_rule(url[0], methods=url[1], view_func=url[2])

app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run(debug=True)
