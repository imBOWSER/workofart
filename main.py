from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your actual secret key
SECRET_KEY = "WRAITH-7XQ9F-G2LMV"

@app.route('/validate-key', methods=['POST'])
def validate_key():
    data = request.json
    key = data.get("key", "")

    if key == SECRET_KEY:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False}), 401  # Unauthorized

if __name__ == "__main__":
    app.run(debug=True)