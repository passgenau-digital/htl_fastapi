# fastapi_demo.py
from fastapi import FastAPI, HTTPException, Path, Query, Body, BackgroundTasks, Depends
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4
from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from typing import List, Optional, Dict

# --------------------------
# 1. DATENMODELLE
# --------------------------

class Book(BaseModel):
    # TODO: Ergänze die Felder mit Validierung
    # - title: string (mind. 2 Zeichen)
    # - author: string (mind. 5 Zeichen)
    # - isbn: string (regex für ISBN-13 Format)
    # - publication_year: int (zwischen 1450 und aktuelles Jahr)
    pass

class Loan(BaseModel):
    # TODO: Ergänze die Felder
    # - user_id: UUID (automatisch generiert)
    # - book_id: UUID
    # - due_date: datetime (mind. 7 Tage in der Zukunft)
    pass

# --------------------------
# 2. FASTAPI-INSTANZ & DATEN
# --------------------------

app = FastAPI()
books: Dict[UUID, Book] = {}
loans: Dict[UUID, Loan] = {}

# --------------------------
# 3. GRUNDLEGENDE ENDPOINTS 
# --------------------------

@app.post("/books", status_code=201)
def create_book(book: Book):
    # TODO: Buch-ID generieren und in 'books' speichern
    # Rückgabe: Buch mit generierter ID
    pass

@app.get("/books")
def get_all_books():
    return list(books.values())

@app.get("/books/{book_id}")
def get_book(book_id: UUID):
    # TODO: Buch suchen und 404-Fehler wenn nicht vorhanden
    pass

# --------------------------
# 4. ERWEITERTE ENDPOINTS
# --------------------------

@app.patch("/books/{book_id}")
def update_book(
    book_id: UUID,
    title: Optional[str] = Body(None),
    author: Optional[str] = Body(None)
):
    # TODO: Teilaktualisierung implementieren
    # - Nur vorhandene Felder aktualisieren
    # - Validierung beachten
    pass

@app.get("/search")
def search_books(
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None)
):
    # TODO: Filterung implementieren
    # - Groß-/Kleinschreibung ignorieren
    # - Kombination von Filtern ermöglichen
    pass

# --------------------------
# 5. HINTERGRUNDTASKS
# --------------------------

def send_overdue_notification(loan_id: UUID):
    # TODO: Logik für Benachrichtigungen
    # - In Datei loggen: "Sent notification for loan {loan_id}"
    pass

@app.post("/loans")
def create_loan(
    loan: Loan, 
    background_tasks: BackgroundTasks
):
    # TODO: 
    # - Fälligkeitsdatum validieren (mind. 7 Tage)
    # - Hintergrundtask für wöchentliche Überprüfung hinzufügen
    pass

# --------------------------
# 6. TESTFÄLLE
# --------------------------

client = TestClient(app)

def test_create_book():
    # TODO: Test für erfolgreiche Buch-Erstellung
    response = client.post(...)
    assert response.status_code == 201
    assert ... 

def test_invalid_isbn():
    # TODO: Test für ungültige ISBN
    pass

# --------------------------
# 7. SERVER-START
# --------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)