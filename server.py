from flask import Flask, render_template

# PROPS
app = Flask(__name__)


# METHODS
@app.route("/")
def home():
    return render_template("index.html")


# MAIN
if __name__ == "__main__":
    app.run(debug=True)
