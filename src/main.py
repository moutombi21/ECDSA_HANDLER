from src.ecdsa_handler import SecureECDSAHandler


def main():
    handler = SecureECDSAHandler()
    handler.save_keys()
    print("Keys generated and saved successfully.")


if __name__ == "__main__":
    main()
