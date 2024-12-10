# ECDSA Handler

## Description

**ECDSA Handler** est une bibliothèque Python qui permet de gérer les clés ECDSA, les signatures numériques, et les tokens JWT (JSON Web Tokens). Elle fournit une interface simple pour générer, sauvegarder, charger des clés cryptographiques, et effectuer des opérations de signature et de vérification.

---

## Fonctionnalités

- Génération de clés ECDSA (privée et publique) basées sur la courbe `SECP256k1`.
- Signature et vérification de données.
- Gestion de tokens JWT avec signature ES256.
- Sauvegarde et chargement des clés au format PEM.
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
from ecdsa_handler import ECDSAHandler, ECDSAHandlerException

if __name__ == "__main__":
    try:
        handler = ECDSAHandler()
        handler.generate_keys()
        handler.save_private_key("private_key.pem")
        handler.save_public_key("public_key.pem")

        data = b"Exemple de données"
        signature = handler.sign(data)
        print(f"Signature valide : {handler.verify(signature, data)}")
    except ECDSAHandlerException as e:
        print(f"Erreur ECDSA : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
```

### Commande pour exécuter :

```bash
python main.py
```

---

## Structure du Projet

```
ECDSA_HANDLER/
├── ecdsa_handler.py         # Classe principale pour gérer les clés ECDSA
├── main.py                  # Point d'entrée principal pour tester la bibliothèque
├── tests/
│   └── test_ecdsa_handler.py # Tests unitaires
├── benchmark.py             # Script de performance
├── requirements.txt         # Liste des dépendances
├── README.md                # Documentation
```

---

## Tests

1. **Exécuter les tests unitaires :**

   ```bash
   python -m unittest discover tests
   ```

2. **Exécuter le benchmark :**

   ```bash
   python benchmark.py
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

- Documentation SECP256k1 : [SECG SEC2](https://www.secg.org/sec2-v2.pdf)
- Documentation ECDSA : [Elliptic Curve Digital Signature Algorithm](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- Bibliothèque `ecdsa` : [PyPI](https://pypi.org/project/ecdsa/)
- JSON Web Tokens (JWT) : [jwt.io](https://jwt.io/)

# ECDSA_HANDLER
