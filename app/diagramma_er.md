erDiagram

    %% Relazioni tra le entità
    CATEGORIEA ||--o{ PRODOTTO : "ha"

    %% Tabella CATEGORIA
    CATEGORIA {
        int id PK
        string nome

    }

    %% Tabella PRODOTTO
    PRODOTTO {
        int id PK
        int categoria_id FK
        string nome
        int prezzo

    }

