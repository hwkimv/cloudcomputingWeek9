from flask import Flask, jsonify, render_template
import json, os

app = Flask(__name__)

# JSON 로더
def load(name):
    with open(os.path.join("data", f"{name}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

# 1) HTML 페이지
@app.get("/")
@app.get("/main")
def main_page():
    return render_template("main.html", data=load("main"))

@app.get("/subject")
def subject_page():
    return render_template("subject.html", data=load("subject"))

@app.get("/rationale")
def rationale_page():
    return render_template("rationale.html", data=load("rationale"))

@app.get("/features")
def features_page():
    return render_template("features.html", data=load("features"))

@app.get("/environment")
def environment_page():
    return render_template("environment.html", data=load("environment"))

@app.get("/team")
def team_page():
    return render_template("team.html", data=load("team"))

# 2) API (JSON)
@app.get("/api/<name>")
def api_page(name):
    try:
        return jsonify(load(name))
    except FileNotFoundError:
        return jsonify({"error": "NOT_FOUND"}), 404

# 헬스체크 (배포용)
@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # 개발용 (도커 밖): http://localhost:8080
    app.run(host="0.0.0.0", port=80)
