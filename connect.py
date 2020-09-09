import requests
import pprint #prettyprint
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath("github/moviedb/"))
from api_keys import *


# HTTP Requests METHODS
"""
GET -> grab data
POST -> add/update data
PATCH
PUT
DELETE
"""
#Endpoint (url) --> GET
#HTTP method needed

"""
Endpoint 

/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=7992f0b292cf5d8d11edfae2b38caca6
"""

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
# r = requests.get(endpoint) #json={"api_key":api_key})
# print(r.status_code)
# print(r.text)


#using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'}
# r = requests.get(endpoint, headers=headers) #json={"api_key":api_key})
# print(r.status_code)
# print(r.text)


#Search Movie Names
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())

if r.status_code in range(200,299):   #good response checker
    data = r.json()
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for results in results:
            _id = results['id']
            print(results['title'], _id)
            movie_ids.add(_id)
        print(list(movie_ids))


output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data) #key value pairs
print(df.head())
df.to_csv(output, index=False)