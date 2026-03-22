import requests

METADATA_URL = "https://api.openbrewerydb.org/v1/breweries/meta"
BREWERYDATA_URL = "https://api.openbrewerydb.org/v1/breweries?page={0}&per_page=1" # page value set based on brewery index

def getBreweryCount():
    # Gather full DB metadata to return brewery count
    rsp = requests.get(METADATA_URL)
    #TODO HANDLE ERRORS
    return rsp.json()["total"] #total count of breweries in openbrewerydb
    

def getBreweryData(breweryIndex):
    # Retrieve specific brewery data based on provided index
    breweryURL = BREWERYDATA_URL.format(breweryIndex)
    rsp = requests.get(breweryURL)
    #TODO HANDLE ERRORS
    return rsp.json()[0]