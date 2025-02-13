from flask import Flask, render_template, request, jsonify
from chatgpt import chat_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = chat_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
