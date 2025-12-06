# -1
```mermaid
flowchart TD
    A((Boshlash)) --> B["keys папкасини yaratish (os.makedirs)"]
    B --> C["RSA private key yaratish (rsa.generate_private_key)"]
    C --> D["Private keyni PEM formatga o'girish"]
    D --> E>private_key.pem fayliga yozish]
    E --> F["Public key yaratish (private_key.public_key)"]
    F --> G["Public keyni PEM formatga o'girish"]
    G --> H>public_key.pem fayliga yozish]
    H --> I["Chop etish: 'Kalitlar yaratildi!'"]
    I --> J((Tugash)) 
```mermaid
classDiagram
    class Signer {
        +main()
        -priv_path : string
        -sig_path : string
        -data_obj : dict/list
        -data_json : bytes
        -signature : bytes
        +load_private_key(path)
        +create_signature(data_json)
        +save_signature(path, signature)
    }

    class JSONHandler {
        +to_json(obj) : bytes
    }

    class KeyLoader {
        +load_private(path) : PrivateKey
    }

    class SignatureCreator {
        +sign(private_key, data_json) : bytes
    }

    class FileWriter {
        +write(path, data)
    }

    Signer --> JSONHandler : uses
    Signer --> KeyLoader : uses
    Signer --> SignatureCreator : uses
    Signer --> FileWriter : uses
