import unittest
from ecdsa_handler import ECDSAHandler, KeyNotLoadedException, InvalidSignatureException


class TestECDSAHandler(unittest.TestCase):
    def setUp(self):
        self.handler = ECDSAHandler()
        self.handler.generate_keys()

    def test_key_save_and_load(self):
        self.handler.save_private_key("test_private_key.pem")
        self.handler.save_public_key("test_public_key.pem")
        new_handler = ECDSAHandler()
        new_handler.load_private_key("test_private_key.pem")
        self.assertEqual(
            self.handler.private_key.to_string(),
            new_handler.private_key.to_string()
        )

    def test_sign_and_verify(self):
        data = b"Test data"
        signature = self.handler.sign(data)
        self.assertTrue(self.handler.verify(signature, data))

    def test_invalid_signature(self):
        data = b"Test data"
        invalid_data = b"Other data"
        signature = self.handler.sign(data)
        with self.assertRaises(InvalidSignatureException):
            self.handler.verify(signature, invalid_data)

    def test_sign_jwt(self):
        claims = {"aud": "https://example.com", "sub": "user@example.com"}
        token = self.handler.sign_jwt(claims)
        verified_claims = self.handler.verify_jwt(token)
        self.assertEqual(claims['aud'], verified_claims['aud'])


if __name__ == "__main__":
    unittest.main()
