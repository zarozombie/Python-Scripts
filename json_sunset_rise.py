#### Import JSON ########
import json

#### Import urllib.request #####
import urllib.request     ## had to specifically call .request

###get JSON as HTML request
response = urllib.request.urlopen('https://api.sunrise-sunset.org/json?lat=42.416822&lng=-83.2465677')
##put request in variable
html = response.read()

##take HTML variable and put in JSON variable (format?
j = json.loads(html.decode("utf-8"))

##Print sunest and sunrise
print("")
print("sunrise")
print(j['results']['sunrise'])
print("")
print("Sunset")
print(j['results']['sunset'])
print("")
