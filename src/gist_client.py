import os
from dotenv import load_dotenv
import requests

# --- CONFIGURATION ---
load_dotenv()
GIST_TOKEN = os.getenv("GIST_TOKEN")
GIST_ID = os.getenv("GIST_ID")
FILE_NAME = "breweriesOfTheDay.json"

URL = url = f"https://api.github.com/gists/{GIST_ID}"

def updateGistData(description, jsonData):
    # Publish new JSON data to Github Gist
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {GIST_TOKEN}",
               "X-GitHub-Api-Version": "2022-11-28"}
    payload = {
        "description": description,
        "files": {
            FILE_NAME: {
                "content": jsonData
            }
        }
    }
    rsp = executePatchRequest(URL, payload, headers)


def executePatchRequest(url, json, headers):
    # Generic function for handling PATCH Requests
    print(f"Executing PATCH request")

    try:
        rsp = requests.patch(url=url, json=json, headers=headers)
        rsp.raise_for_status()

        return rsp

    except requests.exceptions.Timeout:
        raise Exception("The request timed out") from None
    except requests.exceptions.ConnectionError:
        raise Exception("Network Connection Error") from None
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error occurred: {err}") from None
    except requests.exceptions.RequestException as err:
        raise Exception(f"An unexpected error occurred: {err}") from None