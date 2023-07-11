from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    try:
        with open("main.html") as f:
            html = f.read()
        return html
    except Exception as e:
        return str(e)
    #return "Sweet" 
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/case')
def case():
    with open("temp.html") as f:
        html = f.read()
    return html
    #return render_template("temp.html")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
