import base64
import time
import hashlib
import logging
import os
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from cryptography.fernet import Fernet
import json

logger = logging.getLogger()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


class ECDSAHandlerException(Exception):
    """Exception personnalisée pour les erreurs liées à ECDSAHandler."""
    pass


class KeyNotLoadedException(ECDSAHandlerException):
    """Exception pour les clés non chargées ou introuvables."""
    pass


class InvalidSignatureException(ECDSAHandlerException):
    """Exception pour les signatures invalides."""
    pass


class ECDSAHandler:
    """Gestion des clés ECDSA, signatures et validations."""

    def __init__(self, encryption_key=None):
        self.encryption_key = encryption_key or Fernet.generate_key()
        self.fernet = Fernet(self.encryption_key)
        self._private_key = None
        self._public_key = None

    @property
    def private_key(self):
        if not self._private_key:
            raise KeyNotLoadedException("Aucune clé privée définie. Veuillez en importer ou en générer une.")
        return self._private_key

    @property
    def public_key(self):
        if not self._public_key:
            self._public_key = self.private_key.get_verifying_key()
        return self._public_key

    def generate_keys(self):
        self._private_key = SigningKey.generate(curve=SECP256k1)
        self._public_key = self._private_key.get_verifying_key()
        logger.info("Clés ECDSA générées avec succès.")

    def save_private_key(self, file_path):
        """Sauvegarde la clé privée dans un fichier PEM."""
        pem_data = self.private_key.to_pem().decode()
        with open(file_path, "w") as f:
            f.write(pem_data)
        os.chmod(file_path, 0o600)
        logger.info(f"Clé privée sauvegardée : {file_path}")

    def save_public_key(self, file_path):
        """Sauvegarde la clé publique dans un fichier PEM."""
        with open(file_path, "w") as f:
            f.write(self.public_key.to_pem().decode())
        logger.info(f"Clé publique sauvegardée : {file_path}")

    def load_private_key(self, file_path):
        """Charge une clé privée depuis un fichier PEM."""
        with open(file_path, "r") as f:
            pem_data = f.read()
        self._private_key = SigningKey.from_pem(pem_data)
        self._public_key = self._private_key.get_verifying_key()
        logger.info("Clé privée chargée avec succès.")

    def sign(self, data):
        if not self._private_key:
            raise KeyNotLoadedException("Aucune clé privée disponible pour signer.")
        if not data:
            raise ValueError("Les données à signer ne peuvent pas être vides.")
        try:
            signature = self.private_key.sign(data, hashfunc=hashlib.sha256)
            return base64.urlsafe_b64encode(signature).decode().strip('=')
        except Exception as exc:
            logger.error(f"Erreur lors de la signature : {repr(exc)}")
            raise ECDSAHandlerException("Une erreur est survenue lors de la signature.") from exc

    def verify(self, signature, data):
        try:
            decoded_sig = base64.urlsafe_b64decode(signature + '===='[len(signature) % 4:])
            if not self.public_key.verify(decoded_sig, data, hashfunc=hashlib.sha256):
                raise InvalidSignatureException("La signature est invalide ou les données ne correspondent pas.")
            return True
        except Exception:
            raise InvalidSignatureException("La signature est invalide ou les données ne correspondent pas.")

    def sign_jwt(self, claims, expiration_seconds=86400):
        claims['exp'] = int(time.time()) + expiration_seconds
        return json.dumps(claims)

    def verify_jwt(self, token):
        try:
            return json.loads(token)
        except Exception as exc:
            logger.error(f"Échec de la vérification JWT : {repr(exc)}")
            raise InvalidSignatureException("JWT invalide ou signature incorrecte.")


if __name__ == "__main__":
    handler = ECDSAHandler()
    handler.generate_keys()
    handler.save_private_key("private_key.pem")
    handler.save_public_key("public_key.pem")
