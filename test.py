url = ""
api_key = "api_live_UVer4qTOKVZy6bi1Xebhe01SQzocf4VaKjRJSdAZADKcYog5qhvG7Z"

import requests as rq 

data = rq.get(f'https://api.apitube.io/v1/news/everything?per_page=50&api_key={api_key}')

print(data.json())