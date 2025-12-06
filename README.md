# -1
## 1. Key Generation Diagram  ## 2. Signer Class Diagram  ## 3. Verifier Flowchart
```mermaid
flowchart TD
    %% Styles
    classDef startEnd fill:#D1FFD6,stroke:#2ECC71,stroke-width:2px,rx:15,ry:15;
    classDef process fill:#E9F3FF,stroke:#4A90E2,stroke-width:2px,rx:10,ry:10;
    classDef io fill:#FFF4D6,stroke:#F5A623,stroke-width:2px,rx:10,ry:10;
    classDef decision fill:#FFE4E1,stroke:#FF6347,stroke-width:2px,rx:10,ry:10;

    %% Blocks
    A((Boshlash)):::startEnd --> 
    B["Yuklash: public_key.pem"]:::io -->
    C["Yuklash: signature.sig"]:::io -->
    D["Data objectni JSON formatga o‘tkazish"]:::process -->
    E{"Imzo tekshiriladi?"}:::decision
    E -->|To‘g‘ri| F["✔ Imzo to‘g‘ri! (VALID)"]:::process
    E -->|Noto‘g‘ri| G["❌ Imzo noto‘g‘ri! (INVALID)"]:::process
    F --> H((Tugash)):::startEnd
    G --> H
```

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
```

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

