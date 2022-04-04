from flask import Flask , render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('index.html')

@app.route("/Login")
def login():
  
    return render_template('Login.html')

@app.route("/Registration")
def Registration():
    
    return render_template('Registration.html')

if __name__ == "__main__":
   app.run(debug=True)