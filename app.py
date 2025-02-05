from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hej! Flask-appen fungerar!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    return jsonify({"response": f"AI säger: {data['message']}"})

if __name__ == "__main__":
    app.run(debug=True)