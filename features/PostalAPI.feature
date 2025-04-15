# Created by joeca at 4/15/2025
Feature: Verify if the Postal API fetches the correct data
  Scenario Outline: Verify full postal to pincode data fetch
  Given the postal data needed as input <city>
  When we execute the Fetch by Postcode API
  Then the correct postcodes are fetched
  Given the pincode data needed
  When we execute the Fetch by Pincode API
  Then the data has the correct pincodes
    Examples:
      | city     |
      | Thane    |
      | China     |
      | Mumbai   |
      |    @123      |
      |     -         |
      |               |
