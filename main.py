from flask import Flask, jsonify, render_template
import os

app = Flask(__name__,  static_folder='static')

app.config['FAVICON'] = 'maple.ico'

@app.route('/')
def index():
    return render_template("heart.html")

@app.route('/test1') 
def test():
    return render_template("adorable_one.html")
    
@app.route('/test2') 
def test():
    return render_template("adorable_two.html")
    
@app.route('/test3') 
def test():
    return render_template("adorable_three.html")

@app.route('/test4') 
def test():
    return render_template("adorable_four.html")

@app.route('/test5') 
def test():
    return render_template("adorable_five.html")

@app.route('/test6') 
def test():
    return render_template("adorable_six.html")

@app.route('/test7') 
def test():
    return render_template("adorable_seven.html")
    
@app.route('/case')
def case():
    with open("temp.html") as f:
        html = f.read()
    return html
    #return render_template("temp.html")
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
