from flask import Flask
import redis

app = Flask(__name__)
db = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    count = db.incr("visits")
    return f"Hello! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)