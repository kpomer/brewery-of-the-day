import sys
import random
import json
import datetime
import api_client


def main(dateString):
    
    inputDate = datetime.datetime.strptime(dateString, "%Y-%m-%d")

    # Gather total count of breweries
    breweryTotalCount = api_client.getBreweryCount()

    breweries_dict = {}
    dateOffset = [-1,0,1] # used to gather data from before/on/after input date (for handling timezones)
    for offset in dateOffset:
        checkDate = inputDate + datetime.timedelta(days=offset)

        checkDateString = checkDate.strftime("%Y-%m-%d")
        random.seed(checkDateString) # "random" breweryIndex is deterministic based on date seed
        breweryIndex = random.randint(1, breweryTotalCount)
        breweryData = api_client.getBreweryData(breweryIndex)
        breweries_dict[checkDateString] = breweryData

    breweriesOfTheDay = json.dumps(breweries_dict, indent=2)
    print(breweriesOfTheDay)

    #TODO Set Gist data




if __name__ == "__main__":
    if len(sys.argv) == 2:
        date_input = sys.argv[1]
        main(date_input)
    else:
        print("Missing date argument!")