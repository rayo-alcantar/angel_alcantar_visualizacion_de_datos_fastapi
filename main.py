from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Configuración de rutas absolutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()

# Configuración de archivos estáticos
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Análisis de Natación Olímpica"})

# Ruta para top países
@app.get("/top-paises", response_class=HTMLResponse)
async def top_paises(request: Request):
    return templates.TemplateResponse("top_paises.html", {"request": request, "title": "Top Países"})

# Ruta para top atletas
@app.get("/top-atletas", response_class=HTMLResponse)
async def top_atletas(request: Request):
    return templates.TemplateResponse("top_atletas.html", {"request": request, "title": "Top Atletas"})

# Ruta para progresión de tiempos
@app.get("/progresion-tiempos", response_class=HTMLResponse)
async def progresion_tiempos(request: Request):
    return templates.TemplateResponse("progresion_tiempos.html", {"request": request, "title": "Progresión de Tiempos"})

# Ruta para nadadores por país
@app.get("/nadadores-por-pais", response_class=HTMLResponse)
async def nadadores_por_pais(request: Request):
    return templates.TemplateResponse("nadadores_por_pais.html", {"request": request, "title": "Nadadores por País"})
