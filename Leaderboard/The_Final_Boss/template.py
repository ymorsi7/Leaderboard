from typing import List, Dict
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Replace with your own Slidespace API URL
SLIDESPACE_API_URL = "https://slidespace.icu/api"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/leaderboard", response_class=HTMLResponse)
async def leaderboard(request: Request):
    # Fetch section and team data from the Slidespace API
    sections = fetch_sections()
    teams = {}
    for section_id in sections.keys():
        teams.update(fetch_teams_for_section(section_id))
    
    # Fetch team details and scores from the Slidespace API
    mvp_data = []
    for team_id, team_name in teams.items():
        team_details = fetch_team_details(team_id)
        team_scores = fetch_team_scores(team_id)
        mvp_data.append({
            "id": team_details["id"],
            "product": team_name,
            "description": team_details["description"],
            "members": team_details["members"],
            "scores": team_scores
        })
    
    # Sort MVP ideas by total score
    mvp_data.sort(key=lambda mvp: sum(mvp["scores"].values()), reverse=True)
    
    # Render the leaderboard template with the MVP data
    return templates.TemplateResponse("leaderboard.html", {"request": request, "mvp_data": mvp_data})

def fetch_sections() -> Dict[str, str]:
    response = requests.get(f"{SLIDESPACE_API_URL}/sections")
    return response.json()["sections"]

def fetch_teams_for_section(section_id: str) -> Dict[str, str]:
    response = requests.get(f"{SLIDESPACE_API_URL}/sections/{section_id}/teams")
    return response.json()["names"]

def fetch_team_details(team_id: str) -> Dict[str, any]:
    response = requests.get(f"{SLIDESPACE_API_URL}/teams/{team_id}")
    return response.json()["team"]

def fetch_team_scores(team_id: str) -> Dict[str, int]:
    response = requests.get(f"{SLIDESPACE_API_URL}/teams/{team_id}/scores")
    return response.json()["scores"]

