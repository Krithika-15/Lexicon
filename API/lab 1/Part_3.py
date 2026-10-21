import os
from dotenv import load_dotenv
from api_client import get_json
import requests
from pprint import pprint


# 3 call the API with the token

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"Bearer {token}"}
github_username = input("Enter github username : ")
url = f"https://api.github.com/users/{github_username}/repos"

repositories = get_json(url, params={"sort": "pushed", "per_page": 5}, headers=headers)
if repositories is None:
    print("Could not get the repositories")
else:
    for repo in repositories:
        print(repo["name"])



# 4 Prove that the token is use
response_1 = requests.get(url, headers=headers, timeout=5)
print("With token: ", response_1.headers["X-RateLimit-Limit"])
# With token:  5000

response_2 = requests.get(url, timeout=5)
print("Without token: ", response_2.headers["X-RateLimit-Limit"])
# Without token:  60


# 5 Bad headers
bad_headers = {"Authorization": f"Bearer {token}bad"}
response_3 = requests.get(url, headers=bad_headers , timeout=5)
print(response_3.status_code)
pprint(response_3.json())
# Test result
# 401
# {'documentation_url': 'https://docs.github.com/rest',
#  'message': 'Bad credentials',
#  'status': '401'}

# 401 means I don't know who you are (unauthorized)
# retrying with valid token can work
# 403 means I know you, but you are not allowed to do (forbidden)
# retrying will not help, as you need more permission.
