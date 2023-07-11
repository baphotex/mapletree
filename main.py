from flask import Flask, jsonify, render_template, send_from_directory
import os

app = Flask(__name__,  static_folder='static')

@app.route('/')
def index():
    return render_template("home_cute.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('maple.ico')

@app.route('/miko')
def mix():
    return render_template("garbage.html") 
    
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
