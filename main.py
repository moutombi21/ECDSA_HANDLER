from ecdsa_handler import ECDSAHandler, ECDSAHandlerException

if __name__ == "__main__":
    try:
        # Initialisation du gestionnaire
        handler = ECDSAHandler()

        # Génération des clés
        handler.generate_keys()

        # Sauvegarde des clés dans des fichiers
        handler.save_private_key("private_key.pem")
        handler.save_public_key("public_key.pem")

        # Exemple de signature et vérification
        data = b"Test data"
        signature = handler.sign(data)
        print(f"Signature valide : {handler.verify(signature, data)}")

    except ECDSAHandlerException as e:
        print(f"Erreur ECDSA : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
