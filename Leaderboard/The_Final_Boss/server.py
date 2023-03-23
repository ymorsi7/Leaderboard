# Necessary Imports
from fastapi.responses import RedirectResponse
from fastapi import FastAPI                   # The main FastAPI import
from fastapi.responses import HTMLResponse    # Used for returning HTML responses
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn                                # Used for running the app
from fastapi import FastAPI, Request, Form
from urllib.request import urlopen
import json
from fastapi.responses import FileResponse


import re

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
    
@app.get("/profile", response_class = HTMLResponse)
def get_library() -> HTMLResponse:
    with open("profile.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/logout")
def handle_logout(request: Request):
    return RedirectResponse(url="/login")

    
def validate_registration_form(student_id, email, username, password):
    if not (100000000 <= student_id <= 999999999):
        return 'Student ID must be a 9-digit number.'

    if not is_valid_email(email):
        return 'Please enter a valid email address.'

    if not is_valid_username(username):
        return 'Username must be at least 6 characters long and contain only letters and numbers.'

    if not is_valid_password(password):
        return 'Password must be at least 8 characters long and have at least one uppercase letter, one lowercase letter, and one number.'

    return None

def is_valid_email(email):
    regex = r'^\S+@\S+\.\S+$'
    return bool(re.match(regex, email))

def is_valid_username(username):
    regex = r'^[a-zA-Z0-9]{6,}$'
    return bool(re.match(regex, username))

def is_valid_password(password):
    regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'
    return bool(re.match(regex, password))




# @app.get('/logo.png', include_in_schema=False)
# async def favicon():
#     return FileResponse("images/logo.png")


@app.get("/logo.png")
async def favicon():
    return FileResponse("images/logo.png", media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6544)
    # 6543

