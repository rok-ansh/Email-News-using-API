import requests

api_key = "178dba6ceaf346018f4c7280d95f99e4"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-09-03&sortBy=publishedAt&apiKey"
       "=178dba6ceaf346018f4c7280d95f99e4")

# Make a request
request = requests.get(url)

# Get a dictionary
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
