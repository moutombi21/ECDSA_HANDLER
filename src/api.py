import sys
from pathlib import Path
from flask import Flask, request, jsonify
from ecdsa_handler import SecureECDSAHandler
import logging

# Ajouter le dossier src au PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent))

app = Flask(__name__)
handler = SecureECDSAHandler()

logging.basicConfig(level=logging.DEBUG)

#@app.before_request
#def log_request_info():
#    logging.debug(f"Headers: {request.headers}")
#    logging.debug(f"Body: {request.get_data()}")


@app.route("/")
def home():
    return jsonify({"message": "Welcome to ECDSA API!"})


@app.route("/sign", methods=["POST"])
def sign_data():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "Data is required"}), 400
    try:
        signature = handler.sign_data(data.encode())
        return jsonify({"signature": signature.hex()}), 200
    except Exception as e:
        return jsonify({"error": f"Error signing data: {str(e)}"}), 500


@app.route("/verify", methods=["POST"])
def verify_signature():
    data = request.json.get("data")
    signature = request.json.get("signature")
    if not data or not signature:
        return jsonify({"error": "Data and signature are required"}), 400
    try:
        is_valid = handler.verify_signature(bytes.fromhex(signature), data.encode())
        return jsonify({"valid": is_valid}), 200
    except ValueError as e:
        return jsonify({"error": f"Invalid signature format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error verifying signature: {str(e)}"}), 500


@app.route("/rotate", methods=["POST"])
def rotate_keys():
    global handler
    try:
        handler = SecureECDSAHandler()  # Regenerate keys
        return jsonify({"message": "Keys rotated successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Error rotating keys: {str(e)}"}), 500
    


if __name__ == "__main__":
    app.run(debug=True)
