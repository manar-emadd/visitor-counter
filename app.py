from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
db = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    count = db.incr("visits")
    return f"Hello! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)