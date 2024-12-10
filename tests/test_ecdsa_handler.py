import unittest
from ecdsa_handler import ECDSAHandler, KeyNotLoadedException, InvalidSignatureException

class TestECDSAHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ECDSAHandler()
        self.handler.generate_keys()

    def test_sign_and_verify(self):
        data = b"Test data"
        signature = self.handler.sign(data)
        self.assertTrue(self.handler.verify(signature, data))

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            self.handler.sign(b"")

    def test_invalid_signature(self):
        data = b"Test data"
        invalid_data = b"Modified data"
        signature = self.handler.sign(data)
        with self.assertRaises(InvalidSignatureException):
            self.handler.verify(signature, invalid_data)

    def test_no_private_key(self):
        self.handler.clear_private_key()
        with self.assertRaises(KeyNotLoadedException):
            self.handler.sign(b"Test data")

    def test_malformed_jwt(self):
        malformed_jwt = "malformed.jwt.token"
        with self.assertRaises(InvalidSignatureException):
            self.handler.verify_jwt(malformed_jwt)

if __name__ == "__main__":
    unittest.main()
