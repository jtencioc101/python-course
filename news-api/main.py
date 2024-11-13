import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=kubernetes&from=2024-10-12&sortBy=publishedAt&"\
      "apiKey=55a07921a3ba48279065a507bd30e1a3"

# Make the request
request = requests.get(url)

# Gets a dictionary with data
content = request.json()

# Access the article description and url
body = ""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)

