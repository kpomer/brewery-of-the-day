import requests

# Data comes from Open Brewery DB (https://www.openbrewerydb.org)
METADATA_URL = "https://api.openbrewerydb.org/v1/breweries/meta"
BREWERYDATA_URL = "https://api.openbrewerydb.org/v1/breweries?page={0}&per_page=1"

def getBreweryCount():
    # Gather DB metadata to return total brewery count
    rsp = executeGetRequest(METADATA_URL)
    return rsp.json()["total"] #total count of breweries in OpenBreweryDB
    

def getBreweryData(breweryIndex):
    # Retrieve specific brewery data based on a provided index
    breweryURL = BREWERYDATA_URL.format(breweryIndex)
    rsp = executeGetRequest(breweryURL)
    return rsp.json()[0]


def executeGetRequest(url):
    # Generic function for handling GET Requests
    print(f"Executing GET request")
    try:
        rsp = requests.get(url)
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