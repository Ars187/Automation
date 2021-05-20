import requests
ccode=input('Enter counrty code: ')
pcode=input('Enter pincode: ')
response=requests.get(f'https://api.zippopotam.us/{ccode}/{pcode}')
json_r=response.json()
country_repo=json_r['country']
place_repo=json_r['places'][0]
print(f'Country: {country_repo}')
print(f'Place Name: {place_repo["place name"]}')
print(f'State: {place_repo["state"]}')
