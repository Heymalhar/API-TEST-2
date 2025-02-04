from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "Welcome to Malhar's first ever server."

@app.route("/upload", methods=['POST'])
def retrieve():

    data = request.form["data"]

    return f"This is the data you entered: {data}"

if __name__ == "__main__":
    app.run()
