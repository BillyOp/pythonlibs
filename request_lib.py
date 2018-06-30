# Request Library and all its functions
import requests
import time

# Open Weathermap API Key = cdf2fb9e7d9be8a6a1ddfddc8cfcee02
# arg :- method, url, *kwargs
# Request Parameters

def main():
    #constants
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    APPID = "cdf2fb9e7d9be8a6a1ddfddc8cfcee02"
    q = 'Nairobi'

    response = makeWeatherRequest(APPID, API_URL, q)
    getWeatherReport(response)

def makeWeatherRequest(APPID, API_URL, q):
    parameters = {
        'APPID': APPID,
        'q':q
    }
    response = requests.get(API_URL, parameters)
    return response

def convertToCelcius(farenheight):
    celcius = abs((farenheight - 32)/1.8)
    return celcius

def getWeatherReport(response):
    weather_data = response.json()
    print("Weather Report for {}".format(weather_data['name']))
    print("Time for the report is: {}".format(time.asctime(time.localtime(weather_data['dt']))))
    print("Current weather in {} is, {}".format(weather_data['name'], weather_data['weather'][0]["description"]))
    print("Temperature: {}".format(convertToCelcius(weather_data['main']['temp_max'])))

if __name__ == '__main__':
    main()


