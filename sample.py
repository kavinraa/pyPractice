import requests
from urllib import response

url = "https://650ab38cdfd73d1fab08bab8.mockapi.io/food"

# to fetch data from the above api server
def FetchData(url):
    a = requests.get(url)
    return a.json()

# Count the number of JSON data present on the server
def CountJSONData(url):
    data = FetchData(url)
    count = 0
    for i in data :
        count = count + 1
    return count

# print(CountJSONData(url))

# Fetching all the names from the API server
def Name(url):
    a = FetchData(url)
    for i in a :
        print(i['name'])

# print(Name(url))

# Fetch data based on ID
def FetchByid(url, id):
    data = FetchData(url)
     # type casting to convert the interger format to string format for ID
    id = str(id)
    for i in data:
        if(i['id']==id):
            print(i['id'])
            print(i['name'])
            print(i['location'])
            print(i['image_url'])

# print(FetchByid(url, 10))

# Fetch Data based on country
def FetchByCountry(url, country):
    data = FetchData(url)
    for i in data :
        if(i['location'] == country):
            print(i['id'])
            print(i['location'])

# FetchByCountry(url,'Vietnam')
            


def FetchByName(url, mockname):
    data = FetchData(url)
    for i in data:
        if(i['name'] == mockname):
            print(i['location'])

#FetchByName(url,'Rachel')
