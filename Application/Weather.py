"""
API key - b18908a653fe6b9f892c5033e26e119b


https://home.openweathermap.org/api_keys

https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API key}

"""

# import module
import requests
import bs4


def weather_api(data):
    city = data['queryResult']['parameters']['geo-city']
    date = data['queryResult']['parameters']['date-time']
    print("--------API----------")
    print(city)
    print("--------API----------")

    # Generating the url
    url = "https://google.com/search?q=weather+" + city
    url = "https://www.google.com/search?q=" + "weather" + city
    # Sending HTTP request
    request_result = requests.get(url).content

    # Pulling HTTP data from internet
    soup = bs4.BeautifulSoup(request_result, "html.parser")

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    str_data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = str_data.split('\n')
    time = data[0]
    sky = data[1]

    output = f"Temperature in {city} is {temp}\n\nTime: {time}\n\nSky Description: {sky}"

    result = {
        'fulfillmentText': output
    }
    print(output)
    return result
