# ECDSA Handler

## Description

**ECDSA Handler** est une bibliothèque Python qui permet de gérer les clés ECDSA, les signatures numériques et les tokens JWT (JSON Web Tokens). Elle utilise désormais des bibliothèques modernes comme `cryptography` et `PyJWT` pour garantir une sécurité accrue et des performances optimales.

---

## Fonctionnalités

- Génération de clés ECDSA (privée et publique) basées sur la courbe `SECP256R1`.
- Signature et vérification de données.
- Gestion de tokens JWT avec signature ES256 via `PyJWT`.
- Sauvegarde et chargement des clés au format PEM avec `cryptography`.
- Gestion des exceptions pour des messages d'erreur clairs.

---

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/moutombi21/ECDSA_HANDLER.git
   cd ECDSA_HANDLER
   ```

2. **Créer un environnement virtuel :**

   ```bash
   python -m venv env
   source env/Scripts/activate   # Windows
   source env/bin/activate       # Linux/Mac
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

### Exemple Basique

Créez un fichier `main.py` avec le contenu suivant pour commencer à utiliser **ECDSA Handler** :

```python
import jwt
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

class ECDSAHandler:
    def __init__(self):
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()

    def sign_data(self, data):
        signature = self.private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        return signature

    def verify_signature(self, signature, data):
        try:
            self.public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
            return True
        except Exception:
            return False

    def sign_jwt(self, claims):
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        return jwt.encode(claims, private_pem, algorithm="ES256")

    def verify_jwt(self, token):
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        return jwt.decode(token, public_pem, algorithms=["ES256"])

if __name__ == "__main__":
    handler = ECDSAHandler()
    data = b"Exemple de données"
    signature = handler.sign_data(data)
    print(f"Signature valide : {handler.verify_signature(signature, data)}")

    claims = {"aud": "test-audience", "exp": 1700000000}
    token = handler.sign_jwt(claims)
    print(f"Token valide : {handler.verify_jwt(token)}")
```

### Commande pour exécuter :

```bash
python main.py
```

---

## Structure du Projet

```
ECDSA_HANDLER/
├── src/
│   ├── ecdsa_handler.py         # Classe principale pour gérer les clés ECDSA
│   ├── api.py                  # API pour utiliser les fonctionnalités via HTTP
├── tests/
│   ├── test_ecdsa_handler.py   # Tests unitaires
├── requirements.txt            # Liste des dépendances
├── setup.py                    # Configuration pour pip et setuptools
├── README.md                   # Documentation
```

---

## Tests

1. **Exécuter les tests unitaires :**

   ```bash
   python -m unittest discover -s tests
   ```

2. **Exécuter un audit de sécurité :**

   ```bash
   pip-audit
   ```

---

## Contribution

### Pour contribuer :

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction :
   ```bash
   git checkout -b feature/ma-fonctionnalite
   ```
3. Faites vos modifications et commitez-les :
   ```bash
   git commit -m "Ajout de ma fonctionnalité"
   ```
4. Poussez vos modifications :
   ```bash
   git push origin feature/ma-fonctionnalite
   ```
5. Ouvrez une Pull Request sur le dépôt principal.

---

## Journalisation et Erreurs

Le projet utilise `logging` pour suivre les activités et signaler les erreurs. Par défaut, les journaux sont affichés dans le terminal avec différents niveaux (`INFO`, `ERROR`).

---

## Auteurs

- **moutombi21** - Développeur Principal

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Ressources

- Documentation SECP256R1 : [SECG SEC2](https://www.secg.org/sec2-v2.pdf)
- Documentation PyJWT : [PyJWT](https://pyjwt.readthedocs.io/)
- Bibliothèque `cryptography` : [cryptography.io](https://cryptography.io/)
- JSON Web Tokens (JWT) : [jwt.io](https://jwt.io/)
