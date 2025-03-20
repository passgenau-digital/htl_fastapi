# demo_fastapi.py
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Dict

# Modell für Item-Validierung
class Item(BaseModel):
    name: str
    price: float
    category: str

# FastAPI-Instanz und Datenstruktur
app = FastAPI()
items: Dict[int, Item] = {
    0: Item(name="Hammer", price=9.99, category="tools"),
    1: Item(name="Nails", price=2.50, category="consumables")
}

# Endpoints
@app.get("/")
def read_root():
    return {"message": "Willkommen zur Inventar-API"}

@app.get("/items")
def get_all_items():
    return items

@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., title="Die ID des Artikels", ge=0)
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    return items[item_id]

@app.post("/items")
def create_item(item: Item):
    new_id = max(items.keys()) + 1 if items else 0
    items[new_id] = item
    return {"id": new_id, **item.dict()}

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    items[item_id] = item
    return {"message": "Artikel aktualisiert", **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Artikel nicht gefunden")
    deleted_item = items.pop(item_id)
    return {"message": "Artikel gelöscht", **deleted_item.dict()}

# Server starten mit: uvicorn demo_fastapi:app --reload