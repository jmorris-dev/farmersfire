from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def check():
    return "you've just been gnomed!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)