from flask import Flask,render_template
app=Flask(__name__)
# create the view for Home Template
@app.route("/")# default page for server
def home():
    return render_template('home.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
@app.route("/data")
def data():
    return render_template('data.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/signup")
def signup():
    return render_template('signup.html')
@app.route("/services")
def services():
    return render_template('services.html')
if __name__=="__main__":
    app.run(debug=True)