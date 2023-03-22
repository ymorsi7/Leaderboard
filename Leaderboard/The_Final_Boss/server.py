# Necessary Imports
from fastapi.responses import RedirectResponse
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app
from fastapi import FastAPI, Request, Form
from urllib.request import urlopen
import json

app = FastAPI()

# Mount the static directory
app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class = HTMLResponse)
def get_html() -> HTMLResponse:
    with open("index.html") as html:
        return HTMLResponse(content=html.read())

@app.get("/leaderboard", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("leaderboard.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/updates", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("updates.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/login", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("login.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/signup", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("signup.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/documentation", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("documentation.html") as html:
        return HTMLResponse(content=html.read())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)

