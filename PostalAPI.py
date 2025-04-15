import configparser

import requests

from payload import getPincodePayload
from utilities.configurations import getConfig
from utilities.resources import APIResources

#get all by post office
postalResponse = requests.get(getConfig()['API']['URL']+APIResources.postofficeEndpoint+getPincodePayload("Thane"))
postalData = postalResponse.json()
postOfficeData = postalData[0]["PostOffice"]

#Validating data
assert postalData[0]["Status"] == "Success"
assert postOfficeData[0]["State"] == "Maharashtra"
pincode = postOfficeData[0]["Pincode"]
print(pincode)

#validate pincode API using the pincode fetched from previous run
pinResponse = requests.get(getConfig()['API']['URL']+APIResources.pincodeEndpoint+getPincodePayload(pincode))
pinData = pinResponse.json()
assert pinData[0]["Status"] == "Success"
pincodeData = pinData[0]["PostOffice"]
for postOffice in pincodeData:
    assert postOffice["Pincode"] == pincode