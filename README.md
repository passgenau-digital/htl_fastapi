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
