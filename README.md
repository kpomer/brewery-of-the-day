# Development Steps

## Add following functionality:

- [x] Call brewery DB metadata API to gather full count of breweries
  - https://api.openbrewerydb.org/v1/breweries/meta

- [x] Use rundate [-1, 0, +1] as seed for random number between 1 and total breweries

- [x] Call the brewery DB once with each seed_value
  - https://api.openbrewerydb.org/v1/breweries?page={seed_value}&per_page=1

- [ ] Store the results in the private Gist

## Next Steps:

- [ ] Setup cron job as Github actions to refresh this data every 24hrs

- [ ] Setup TRMNL plug-in to retrieve this data from the Gist based on the current day
