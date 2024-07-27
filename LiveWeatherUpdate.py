import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/50.06,19.94?par=google&temp=c")

soup = BeautifulSoup(htmldata, 'html.parser')

current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")

chances_rain = soup.find_all("div", class_="CurrentConditions--precipValue--2aJSf")

temp = current_temp[0].text if current_temp else "N/A"
rain = chances_rain[0].text if chances_rain else "N/A"

result = (f"Current temperature: {temp} in Kraków \n Chance of rain:  {rain}")

n.show_toast("Live Weather Update", result, duration=10)
