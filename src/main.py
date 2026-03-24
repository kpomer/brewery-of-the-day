import sys
import random
import json
import datetime
import api_client
import gist_client

def main(dateString):
    
    inputDate = datetime.datetime.strptime(dateString, '%Y-%m-%d') # Reference Date for Data Retrieval
    print(f"Updating Breweries based on reference date: {dateString}")

    breweries_dict = {}
    # Retrieve brewery data for dates around inputDate (including several days before/after to avoid daily updates and handle all timezones)
    breweryTotalCount = api_client.getBreweryCount() # Total count of breweries in DB
    for offset in range(-2, 10):
        checkDate = inputDate + datetime.timedelta(days=offset)
        checkDateString = checkDate.strftime('%Y-%m-%d')

        random.seed(checkDateString) # "random" breweryIndex is deterministic based on checkDateString seed value
        breweryIndex = random.randint(1, breweryTotalCount)
        print(f"Retrieving Brewery Data for Index {breweryIndex}...")
        breweryData = api_client.getBreweryData(breweryIndex)
        breweries_dict[checkDateString] = breweryData

    breweriesOfTheDay = json.dumps(breweries_dict, indent=2)

    # Publish Data to Github Gist
    gistDescription = f"Brewery Data - Updated {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    gist_client.updateGistData(gistDescription, breweriesOfTheDay)


if __name__ == "__main__":
    date_input = ""
    if len(sys.argv) == 1:
        # No date argument - use current date
        date_input = datetime.datetime.now().strftime('%Y-%m-%d')
    elif len(sys.argv) == 2:
        # Use date provided as argument
        date_input = sys.argv[1]
    else:
        print(f"Invalid Number of Arguments: {len(sys.argv)}")
    
    try:
        main(date_input)
        print(f"Brewery Data has been updated!")
    except Exception as e:
        print(e)
        sys.exit(1)