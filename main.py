import requests
from send_email import get_email

api_key = "178dba6ceaf346018f4c7280d95f99e4"
topic = "amazon"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-09-03&sortBy=publishedAt&apiKey"
       "=178dba6ceaf346018f4c7280d95f99e4&language=en")

# Make a request
request = requests.get(url)

# Get a dictionary
content = request.json()

# Access the article titles and description
body = ""
# print(type(body))
for article in content["articles"][:20]:
    if article["description"] is not None:
        body = (f"Subject : Today's {topic.title()} News" + "\n" + body + article["title"] + "\n" +
                article["description"] + "\n" +
                article["url"] + "\n" +
                100*"-" + 2*"\n")

body = body.encode("utf-8")
# message = f"""\
# Subject : Today's {topic.title()} News
# {body}
# """
get_email(body)
print("Mail Sent")
