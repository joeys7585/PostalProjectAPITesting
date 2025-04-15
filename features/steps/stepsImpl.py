from behave import *
import requests

from payload import *
from utilities.configurations import getConfig
from utilities.resources import APIResources


@given('the postal data needed as input {city}')
def step_impl(context, city):
    context.url = getConfig()['API']['URL'] + APIResources.postofficeEndpoint + getPostalPayload(city)

@when(u'we execute the Fetch by Postcode API')
def step_impl(context):
    context.postalResponse = requests.get(context.url)

@then(u'the correct postcodes are fetched')
def step_impl(context):
    postalData = context.postalResponse.json()
    postOfficeData = postalData[0]["PostOffice"]
    assert postalData[0]["Status"] == "Success"
    assert postOfficeData[0]["State"] == "Maharashtra"
    context.pincode = postOfficeData[0]["Pincode"]
    print(context.pincode)

@given(u'the pincode data needed')
def step_impl(context):
    context.pin_url = getConfig()['API']['URL'] + APIResources.pincodeEndpoint + getPincodePayload(context.pincode)

@when(u'we execute the Fetch by Pincode API')
def step_impl(context):
    context.pinResponse = requests.get(context.pin_url)

@then(u'the data has the correct pincodes')
def step_impl(context):
    pinData = context.pinResponse.json()
    assert pinData[0]["Status"] == "Success"
    pincodeData = pinData[0]["PostOffice"]
    for postOffice in pincodeData:
        assert postOffice["Pincode"] == context.pincode