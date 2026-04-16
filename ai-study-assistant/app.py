from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    return jsonify({
        "reply": f"AI Response:\n\nYou asked about '{user_input}'.\nThis is a demo explanation for learning purposes."
    })

@app.route("/notes", methods=["POST"])
def notes():
    topic = request.json["topic"]
    return jsonify({
        "notes": f"Notes on {topic}:\n\n- Definition\n- Key Points\n- Examples\n- Conclusion"
    })

@app.route("/mcq", methods=["POST"])
def mcq():
    topic = request.json["topic"]
    return jsonify({
        "mcq": f"MCQs on {topic}:\n\n1. What is {topic}?\nA) Option 1\nB) Option 2\nAnswer: A"
    })

if __name__ == "__main__":
    app.run(debug=True)