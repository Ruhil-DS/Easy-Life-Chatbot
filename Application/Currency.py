import requests
"""
API key - 9YzmAOEyGS7fxZRxXGriFM1NK5SUyQzK

https://apilayer.com/marketplace/exchangerates_data-api#documentation-tab

"""


def currency_converter(data):
    try:
        curr_amt = data['queryResult']['parameters']['unit-currency']['amount']

        convert = data['queryResult']['parameters']['unit-currency']['currency']

        into = data['queryResult']['parameters']['currency-name'][0]

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={into}&from={convert}&amount={curr_amt}"
        headers = {
            "apikey": "9YzmAOEyGS7fxZRxXGriFM1NK5SUyQzK"
        }
        response = requests.request("GET", url, headers=headers, data={})
        print("-------API RESPONSE-------")
        print(response.text)
        print("-------API RESPONSE-------")

        converted_amt = round(response.json()["result"], 2)

        result = {
            'fulfillmentText': f"{curr_amt} {convert} is {converted_amt} {into}"
        }

        return result

    except KeyError:
        return {
            'fulfillmentText': "My abilities didn't allow me to do that this time. try again? :("
        }




