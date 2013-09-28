from flask import Flask
app = Flask(__name__)

@app.route("/v1/event/put",methods=['POST'])
def hello():
    return "Hello World!"
