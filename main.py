from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/plot")
def plot():
    return render_template("plotapp.html")
    
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
    
