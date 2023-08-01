from flask import Flask, jsonify, request, render_template, send_from_directory
import os

app = Flask(__name__,  static_folder='static')

def ep(start, end, ep_display = False, low = 13, high = 30):
    y = list(range(start,end+1))
    z = len(y)
    string = (
    f"there are  {z} episodes left.\n"
    f"it will take {z*24/60} to {z*30/60} hours to finish watching.\n"
    f"that's only {round(z*24/60/24,2)} to {round(z*30/60/24,2)} days! \n"
    f"based on kasey's habits, it will take {round(z/high,2)} to {round(z/low,2)} days to complete. goodluck!\n"
    ) 
    return string 

@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("maple_home.html", response = '^_^')
    try:    
        start = request.form.get("startep")
        end = request.form.get("endep")
        start = int(start)
        end = int(end)
        if end > 10_000:
            string = "Too many episodes gyabo!" 
            return render_template("maple_home.html", response = string)
        string = ep(start,end) 
    except:
        string = "Uh oh! Those weren't the right kind of numbers :(" 
    return render_template("maple_home.html", response = string)
    
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

@app.route('/reviews/marriage_of_convenience') 
def moc():
    return render_template("review_moc_2.html") 

@app.route('/vent') 
def vent():
    return render_template("vent.html") 


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
