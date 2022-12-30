from flask import Flask, request, jsonify
from Application.Currency import *
from Application.Query import *
from Application.Weather import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def backend():
    if request.method == 'GET':
        return "<h2>This is an API. No other view available</h2>"

    elif request.method == 'POST':
        data = request.get_json()

        intent = data["queryResult"]["intent"]["displayName"]

        if intent.lower() == 'query':
            result = query_func(data)
        elif intent.lower() == 'weather':
            result = weather_api(data)
        elif intent.lower() == 'currency':
            result = currency_converter(data)

        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=8000)


