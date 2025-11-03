from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/hello")
def hello():
    return jsonify({"message": "Hello from ECS + ECR demo!"})

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8001)
