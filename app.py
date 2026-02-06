from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/test", methods=['POST'])
def api_test():
    data = request.get_json()
    message = data['message']

    return jsonify({
        "reply": f"Response: {message}"
    })

@app.route("/greetings")
def greeting():
    return "<h1>Hey, I am Jwal. Who are you...!!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
