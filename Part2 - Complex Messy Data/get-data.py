import requests
import json
import time

#get data from the Best Buy API

# laptop = '(categoryPath.id=abcat0502000)'
# desktop = '(categoryPath.id=abcat0501000)'
# phones = '(categoryPath.id=pcmcat209400050001)'

laptop = 'abcat0502000'
desktop = 'abcat0501000'
phones = 'pcmcat209400050001'
baseURL = 'https://api.bestbuy.com/v1/products'
categoryId = f'(categoryPath.id={desktop})'
apiKey = '***REMOVED***'
sortOptions = '&sort=.asc'
pagination = '100'
responseFormat = 'json'

page = 2
filename= f"desktop-data-{page}.json"

URL= f"{baseURL}({categoryId})?apiKey={apiKey}&pageSize={pagination}&page={page}&format={responseFormat}" 

top10 = f"https://api.bestbuy.com/beta/products/mostViewed(categoryId={desktop})?apiKey={apiKey}"


def save(data, filename="all-laptop-data.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
      
response=requests.get(URL)

if response.status_code==200:
        data=response.json()
        save(data, filename)
else:
        print(f"Failed : {response.status_code}")

