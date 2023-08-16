import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter name of the city\n")
url=f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
r=requests.get(url)
wdic=json.loads(r.text)
text="the cuurent weather of ",{city}, " is ",wdic["current"]["temp_c"],"and",wdic["current"]["temp_f"],"It is last updated at",wdic["current"]["last_updated"]
speak.Speak(text)