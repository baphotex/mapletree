from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    try:
        return Flask.render_template("home.html")
    except Exception, e:
        return str(e)
    #return "Sweet" 
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
