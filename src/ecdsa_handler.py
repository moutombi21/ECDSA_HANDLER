import jwt
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ECDSAHandlerException(Exception):
    pass


class SecureECDSAHandler:
    def __init__(self):
        logger.info("Generating new ECDSA key pair.")
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_key_path="private_key.pem", public_key_path="public_key.pem"):
        private_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(private_key_path, "wb") as priv_file, open(public_key_path, "wb") as pub_file:
            priv_file.write(private_bytes)
            pub_file.write(public_bytes)
        logger.info(f"Keys saved: {private_key_path}, {public_key_path}")

    def sign_data(self, data: bytes) -> bytes:
        logger.info(f"Signing data: {data}")
        return self.private_key.sign(data, ec.ECDSA(hashes.SHA256()))

    def verify_signature(self, signature: bytes, data: bytes) -> bool:
        try:
            self.public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
            logger.info("Signature verified successfully.")
            return True
        except InvalidSignature:
            logger.error("Signature verification failed.")
            return False

    def generate_jwt(self, claims: dict) -> str:
        private_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        logger.info(f"Generating JWT for claims: {claims}")
        return jwt.encode(claims, private_bytes, algorithm="ES256")

    def verify_jwt(self, token: str) -> dict:
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        try:
            decoded = jwt.decode(token, public_bytes, algorithms=["ES256"])
            logger.info("JWT verified successfully.")
            return decoded
        except jwt.PyJWTError as e:
            logger.error(f"JWT verification failed: {e}")
            raise ECDSAHandlerException(f"JWT invalid: {e}")
