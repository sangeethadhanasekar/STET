from flask import Flask,render_template,request

app = Flask(__name__,
 template_folder="temp",
    static_folder="static")

@app.route('/',methods=['GET',"POST"])
def login():
   return render_template("login.html")

@app.route('/signup',methods=['GET',"POST"])
def signup():
   return render_template("signup.html")

@app.route('/header',methods=['GET',"POST"])
def header():
   return render_template("home.html")

if __name__ == "__main__":
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run(debug=True)