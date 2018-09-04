#Que1-->Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
response=requests.get("https://api.forismatic.com/api/1.0/?\
                        method=getQuote&lang=en&format=jsonp&jsonp=?")
print(response.content)
