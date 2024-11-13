import requests
from send_email import send_email

topic = "kubernetes"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&"\
      "apiKey=55a07921a3ba48279065a507bd30e1a3" \
      "&language=en"

# Make the request
request = requests.get(url)

# Gets a dictionary with data
content = request.json()

# Access the article description and url
body = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = "Subject: Today's news" + "\n" \
            + body + article["title"] + "\n" \
            + article["description"] + "\n" \
            + article["url"]  + 2*"\n"

body = body.encode("utf-8")
send_email(body)

