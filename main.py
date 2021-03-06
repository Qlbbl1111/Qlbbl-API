import json
import flask
from flask_restful import Resource, Api, reqparse
import random
import json
from flask import jsonify, request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)
gifs_database = open("gifs.json")

gifs = json.loads(gifs_database.read())

length = len(gifs)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hazbin Images API</h1>
<p>Holy crap Lois! Qlbbl made an API!</p>'''


@app.route('/v1/hazbin/gif/all', methods=['GET'])
def api_all():

    return jsonify(gifs)


@app.route('/v1/hazbin/gif/random', methods=['GET'])
def api_random():

    return jsonify(gifs[random.randint(0, length)])


@app.route('/v1/swim', methods=['POST', 'GET'])
def process_form():
    if request.method == 'POST':
        data = request.form
        swimdata = data['swim']
        if swimdata.lower() == 'true':
            x = "true"
            with open(f'swim.json', 'w') as f:
                f.write(f"{{\"isswim\":{x}}}")
        elif swimdata.lower() == 'false':
            x = "false"
            with open(f'swim.json', 'w') as f:
                f.write(f"{{\"isswim\":{x}}}")
        else:
            pass
        with open(f'swim.json', 'r') as f:
            y = f.read()
            z = json.loads(y)
            j = z.get("isswim")
        return str(j)
    elif request.method == 'GET':
        with open(f'swim.json', 'r') as f:
            y = f.read()
            z = json.loads(y)
            j = z.get("isswim")
        return str(j)
    else:
        pass  



if __name__ == '__main__':
    app.run()