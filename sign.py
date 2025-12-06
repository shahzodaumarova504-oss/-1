# signer.py
import json
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def main():
    # Автоматик йўллар
    priv_path = "keys/private_key.pem"
    sig_path = "signature.sig"

    # SIGN қиладиган Python объект (list/dict)
    data_obj = {
        "name": "Shahzoda",
        "age": 21,
        "subjects": ["Math", "CyberSecurity", "Python"]
    }
    # Ёки:
    # data_obj = [1, 2, 3, 4, 5]

    # JSON строка
    data_json = json.dumps(data_obj, sort_keys=True).encode("utf-8")

    # Приват калитни юклаш
    with open(priv_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Имзо яратиш
    signature = private_key.sign(
        data_json,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    with open(sig_path, "wb") as f:
        f.write(base64.b64encode(signature))

    print("Imzo yaratildi →", sig_path)
    print("JSON imzolangan:", data_obj)

if __name__ == "__main__":
    main()
