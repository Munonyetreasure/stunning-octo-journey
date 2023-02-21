from flask import Flask

app = Flask(__name__)

@app.route("/dashboard")
def dash():
    house= ["2bedroom", "3bedroom", "4bedroom", "5bedroom"]
    return house[0]

app.run()