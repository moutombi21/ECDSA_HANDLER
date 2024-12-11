from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from ecdsa_handler import ECDSAHandler, InvalidSignatureException

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

handler = ECDSAHandler()
handler.generate_keys()


@app.route("/")
def home():
    return jsonify({
        "endpoints": {
            "/sign": "POST - Signer des données",
            "/verify": "POST - Vérifier une signature",
            "/rotate": "POST - Remplacer les clés"
        },
        "message": "Bienvenue sur l'API ECDSA Handler"
    })


@app.route("/sign", methods=["POST"])
@limiter.limit("10 per minute")
def sign_data():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "Les données sont requises"}), 400
    try:
        signature = handler.sign(data.encode())
        return jsonify({"signature": signature}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/rotate", methods=["POST"])
@limiter.limit("2 per hour")
def rotate_keys():
    try:
        handler.rotate_keys(passphrase="monpassphrase")
        return jsonify({"message": "Clés remplacées avec succès"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
