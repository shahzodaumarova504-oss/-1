# verifier.py
import json
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def main():
    pub_path = "keys/public_key.pem"
    sig_path = "signature.sig"

    # ТЕКШИРИЛАДИГАН Python dict/list
    data_obj = {
        "name": "Shahzoda",
        "age": 21,
        "subjects": ["Math", "CyberSecurity", "Python"]
    }
    # data_obj = [1, 2, 3, 4, 5]

    data_json = json.dumps(data_obj, sort_keys=True).encode("utf-8")

    # Публик калитни юклаш
    with open(pub_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Имзони ўқиш
    with open(sig_path, "rb") as f:
        signature = base64.b64decode(f.read())

    try:
        public_key.verify(
            signature,
            data_json,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("✔ Imzo to‘g‘ri! (VALID)")
    except Exception:
        print("❌ Imzo noto‘g‘ri! (INVALID)")

if __name__ == "__main__":
    main()
