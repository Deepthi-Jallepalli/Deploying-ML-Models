from flask import Flask, jsonify, request
from werkzeug import EnvironBuilder 
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        req_json = request.get_json()
        return jsonify({'requested json':req_json}), 201
    else:
        return jsonify({"message":"Hello World"})

if __name__ == '__main__':
    app.run(debug=True)
