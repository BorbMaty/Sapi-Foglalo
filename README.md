
# SapiFoglaló 

Egy egyszerű és felhasználóbarát webalkalmazás, amely lehetővé teszi termek foglalását egy adott dátumra és időpontra. A projekt célja a teremfoglalási folyamat digitalizálása, gyorsabbá és átláthatóbbá tétele.

## Funkciók

- **Felhasználók kezelése**: bejelentkezések kezelése.
- **Termek kezelése**: Termek manuális hozzáadása, listázása és az elérhetőségük megtekintése.
- **Foglalások**: Termek foglalása adott időpontra, foglalások szűrése dátum alapján.
- **Szabad és foglalt időpontok megjelenítése**: Egy terem kiválasztása után a rendszer listázza az adott dátumra vonatkozó szabad és foglalt időpontokat.

## Használt technológiák

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/)
- **Frontend**: HTML, CSS, JavaScript
- **Adatbázis**: Azure MySQL
- **Egyéb**: Pydantic az adatvalidációhoz

## Telepítés

1. Klónozd a projektet:
   ```bash
   git clone https://github.com/BorbMaty/Sapi-Foglalo.git
   cd Sapi-Foglalo
   ```

2. Hozd létre a virtuális környezetet és telepítsd a függőségeket:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```


   ```

5. Indítsd el a fejlesztői szervert:
   ```bash
   uvicorn app.api.main:app --reload
   ```


A FastAPI automatikusan generált dokumentációját itt érheted el:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Projektstruktúra

```
teremfoglalos/
├── app/
│   ├── api/         # FastAPI végpontok
│   ├── db_init.py   # Adatbázis inicializálása
│   ├── models/      # SQLAlchemy modellek
│   ├── schemas/     # Pydantic modellek
├── requirements.txt # Függőségek listája
└── README.md        # Dokumentáció
```

## Fejlesztői csapat

A projektet egyetemi csapatunk fejlesztette, célunk az volt, hogy gyakorlati tapasztalatot szerezzünk a modern webfejlesztés területén. 💡

