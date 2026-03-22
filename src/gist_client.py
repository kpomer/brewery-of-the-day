import os
from dotenv import load_dotenv
import requests

# --- CONFIGURATION (from .env) ---
load_dotenv()
GIST_TOKEN = os.getenv("GIST_TOKEN")
GIST_ID = os.getenv("GIST_ID")
FILE_NAME = "breweriesOfTheDay.json"

URL = url = f"https://api.github.com/gists/{GIST_ID}"



def updateGistData(jsonData):
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {GIST_TOKEN}",
               "X-GitHub-Api-Version": "2022-11-28"}
    payload = {
        "files": {
            FILE_NAME: {
                "content": jsonData
            }
        }
    }
    rsp = requests.patch(url=URL, json=payload, headers=headers)
    #TODO Handle errors
