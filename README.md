# ECDSA Handler API

This project implements an ECDSA (Elliptic Curve Digital Signature Algorithm) API to sign, verify, and manage cryptographic keys. The API is built using Flask and is designed for ease of use.

## Features
- Generate and manage ECDSA keys.
- Sign data using private keys.
- Verify data signatures with public keys.
- Rotate keys dynamically.

## Endpoints

### 1. `/` (GET)
- **Description**: Welcome endpoint to confirm the API is running.
- **Response**:
  ```json
  {
      "message": "Welcome to ECDSA API!"
  }
  ```

### 2. `/sign` (POST)
- **Description**: Sign the provided data using the private key.
- **Request Body**:
  ```json
  {
      "data": "message_to_sign"
  }
  ```
- **Response**:
  ```json
  {
      "signature": "308201..."
  }
  ```

### 3. `/verify` (POST)
- **Description**: Verify the provided signature and data using the public key.
- **Request Body**:
  ```json
  {
      "data": "message_to_sign",
      "signature": "308201..."
  }
  ```
- **Response**:
  ```json
  {
      "valid": true
  }
  ```

### 4. `/rotate` (POST)
- **Description**: Regenerate ECDSA keys.
- **Response**:
  ```json
  {
      "message": "Keys rotated successfully"
  }
  ```

## Prerequisites
- Python 3.8+
- Virtual environment for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ECDSA_HANDLER.git
   cd ECDSA_HANDLER
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. Navigate to the `src` directory and start the server:
   ```bash
   python api.py
   ```

2. The API will be available at `http://127.0.0.1:5000/`.

## Testing

### Run Unit Tests
Execute the following command to run all unit tests:
```bash
python -m unittest discover -s tests
```

## Example Usage

### Using `curl`

1. Test the home endpoint:
   ```bash
   curl -X GET http://127.0.0.1:5000/
   ```

2. Sign data:
   ```bash
   curl -X POST http://127.0.0.1:5000/sign -H "Content-Type: application/json" -d '{"data": "message_to_sign"}'
   ```

3. Verify a signature:
   ```bash
   curl -X POST http://127.0.0.1:5000/verify -H "Content-Type: application/json" -d '{"data": "message_to_sign", "signature": "308201..."}'
   ```

4. Rotate keys:
   ```bash
   curl -X POST http://127.0.0.1:5000/rotate
   ```

## Directory Structure
```
ECDSA_HANDLER/
├── src/
│   ├── api.py                # API implementation
│   ├── ecdsa_handler.py      # ECDSA key handling logic
│   ├── private_key.pem       # Private key (generated dynamically)
│   ├── public_key.pem        # Public key (generated dynamically)
├── tests/
│   ├── test_ecdsa_handler.py # Unit tests
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── .gitignore                # Git ignore file
```

## License
This project is licensed under the MIT License.