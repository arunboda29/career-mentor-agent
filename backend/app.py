from flask import Flask, request, jsonify
from flask_cors import CORS

from career_engine import recommend, get_all_pathways
from mentor import generate_mentor_reply


app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return jsonify({
        "message": "Career Mentor Agent API is running",
        "status": "success"
    })


@app.get("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Career Mentor Agent"
    })


@app.get("/api/pathways")
def pathways():
    return jsonify({
        "count": len(get_all_pathways()),
        "pathways": get_all_pathways()
    })


@app.post("/api/recommend")
def recommendations():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "No student profile was provided."
            }), 400

        if not data.get("name"):
            data["name"] = "Student"

        result = recommend(data)

        return jsonify(result)

    except Exception as error:
        return jsonify({
            "error": "Unable to generate recommendations.",
            "details": str(error)
        }), 500


@app.post("/api/chat")
def chat():
    try:
        data = request.get_json(silent=True) or {}
        message = str(data.get("message", "")).strip()

        if not message:
            return jsonify({"error": "A message is required."}), 400

        answer = generate_mentor_reply(
            message=message,
            history=data.get("history", []),
            profile=data.get("profile"),
            results=data.get("results"),
        )

        return jsonify({"reply": answer})

    except RuntimeError as error:
        return jsonify({"error": str(error)}), 503
    except Exception as error:
        return jsonify({
            "error": "Unable to generate a mentor response.",
            "details": str(error)
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "API endpoint not found."
    }), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "error": "Internal server error."
    }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )