from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    try:
        return render_template("main.html")
    except Exception as e:
        return str(e)
    #return "Sweet" 
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/case')
def case():
    return render_template("temp.html")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
