import requests

# Data comes from Open Brewery DB (https://www.openbrewerydb.org)
METADATA_URL = "https://api.openbrewerydb.org/v1/breweries/meta"
BREWERYDATA_URL = "https://api.openbrewerydb.org/v1/breweries?page={0}&per_page=1"

def getBreweryCount():
    # Gather DB metadata to return total brewery count
    rsp = requests.get(METADATA_URL)
    #TODO HANDLE ERRORS
    return rsp.json()["total"] #total count of breweries in OpenBreweryDB
    

def getBreweryData(breweryIndex):
    # Retrieve specific brewery data based on a provided index
    breweryURL = BREWERYDATA_URL.format(breweryIndex)
    rsp = requests.get(breweryURL)
    #TODO HANDLE ERRORS
    return rsp.json()[0]