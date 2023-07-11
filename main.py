from flask import Flask, jsonify, render_template
import os

app = Flask(__name__,  static_folder='static')

app.config['FAVICON'] = 'maple.ico'

@app.route('/')
def index():
    return render_template("home_cute.html")

@app.route('/bio') 
def bio():
    return render_template("bio_cute.html") 

@app.route('/blog') 
def blog():
    return render_template("blog_cute.html") 
 
@app.route('/test6') 
def test6():
    return render_template("adorable_six.html")

@app.route('/test7') 
def test7():
    return render_template("adorable_seven.html")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
