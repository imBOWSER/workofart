from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your actual secret key
SECRET_KEY = "1234-5678-9101"

@app.route('/validate-key', methods=['POST'])
def validate_key():
    data = request.get_json()  # Use get_json() instead of request.json
    if not data:
        return jsonify({"error": "Invalid request, JSON body required"}), 400

    key = data.get("key", "")
    if key == SECRET_KEY:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False}), 401  # Unauthorized

if __name__ == "__main__":
    app.run(debug=True)
