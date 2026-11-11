from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hola_mundo():
    return "<h1>Hola mundo</h1> <p>Mi primer proyecto del roadmap</p>"

if __name__ == "__main__":
    app.run(debug=True)