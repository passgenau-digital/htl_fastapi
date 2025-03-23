# Introduction to REST-APIs with fastapi

Introductory slides on creating a REST-API in python with the [fastapi framework](https://fastapi.tiangolo.com/).

## How create and run the Presentation

To run the presentation from the [`fastapi_tutorial.ipynb`](fastapi_tutorial.ipynb) use these commands:

First clone the reveal.js into your project folder:

```bash
git clone https://github.com/hakimel/reveal.js.git
```

Then create the reveal.js HTML slideshow:

```bash
// on mac you have to export the jupyter path:
// $ export JUPYTER_PATH=/opt/homebrew/share/jupyter:$JUPYTER_PATH
jupyter-nbconvert fastapi_tutorial.ipynb --to slides --reveal-prefix reveal.js
```

To host the slideshow directly in the browser use the `--post serve` parameter:

```bash
jupyter-nbconvert fastapi_tutorial.ipynb --to slides --reveal-prefix reveal.js --post serve
```

## demo_fastapi.py

### Server starten
```bash
uvicorn demo_fastapi:app --reload
```

### Endpoint-Docu

1. Server starten
2. Unter: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) können die Endpoints eingesehen und getestet werden.


### Beispiel-Requests:
```bash
GET    http://localhost:8000/items
GET    http://localhost:8000/items/0
POST   http://localhost:800/items (Body: JSON mit name/price/category)
PUT    http://localhost:8000/items/0 (Body: aktualisierte Werte)
DELETE http://localhost:8000/items/0
```

## fastapi_student_project.py

### Aufgabenstellungen

1. Vervollständige die Datenmodelle
 - Implementiere die Validierungslogik in den Pydantic-Modellen
 - Nutze Field, validator und Regex
2. Implementiere die fehlenden Endpoints
 - Folgende Funktionen sind unvollständig:
   - create_book()
   - get_book()
   - update_book()
   - search_books()
   - create_loan()
3. Erweitere die Fehlerbehandlung
 - Füge HTTPException für fehlende Ressourcen hinzu
 - Validiere Eingabeparameter
4. Vervollständige die Testfälle
 - Implementiere test_create_book() und test_invalid_isbn()
 - Füge weitere sinnvolle Tests hinzu
5. Zusatzaufgaben
 - Implementiere einen DELETE-Endpoint für Bücher
 - Füge Paginierung zum GET /books-Endpoint hinzu
 - Erstelle einen Middleware für Request-Logging

### Starthilfe:
```bash
Copy
# Server starten (nach Implementierung)
uvicorn fastapi_demo:app --reload

# Tests ausführen (nach Implementierung)
pytest fastapi_demo.py
```

### Kommentierte Stellen:
 - `TODO`: Studenten ergänzen hier → Hauptimplementierungsstellen
 - `pass` → Fehlende Funktionskörper
 - Unvollständige Modelle → `Book` und `Loan`-Klassen
 - Fehlende Validierungslogik → `validator`-Methoden
 - Unvollständige Testfälle → `test_*` Funktionen

*Das Script enthält 17 Stellen die ergänzt werden müssen, um eine voll funktionsfähige API zu erhalten.*

### Musterlösung

```bash
# Server starten
uvicorn fastapi_demo:app --reload

# Tests ausführen
pytest fastapi_demo.py

# Beispiel-Request mit curl:
curl -X POST http://localhost:8000/books -H "Content-Type: application/json" -d '{
  "title": "Domain-Driven Design",
  "author": "Eric Evans",
  "isbn": "978-0-321-12521-7",
  "publication_year": 2003
}'
```