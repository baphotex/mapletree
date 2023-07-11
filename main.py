from flask import Flask, jsonify, render_template, send_from_directory
import os

app = Flask(__name__,  static_folder='static')

def ep(start, end, ep_display = False, low = 12, high = 25):
    y = list(range(start,end+1))
    z = len(y)
    string = f'''
    There are {z} episodes left.
    It will take {z*24/60} to {z*30/60} hours to finish watching.
    It will take {round(z*24/60/24,2)} to {round(z*30/60/24,2)} days to finish watching
    Based on current habits, it will take {round(z/high,2)} to {round(z/low,2)} days to finish.''' 
    return string 

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        start = request.form.get("startep")
        end = request.form.get("endep") 
        try: 
            start = int(start)
            end = int(end)
            string = ep(start,end) 
        except TypeError as e: 
            string = "Uh oh! Those weren't the right kind of numbers :(" 
        return render_template("maple_home.html", response = string) 
    return render_template("maple_home.html", response = '')

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
