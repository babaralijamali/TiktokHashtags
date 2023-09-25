import requests
from bs4 import BeautifulSoup

# Get TikTok video link from the user
url = input("Enter TikTok video link: example:_ https://www.tiktok.com/@babar_ali_jamali/video/7271746480271133958 ")

# Send a GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find hashtags
    hashtags = soup.select('a[href^="/tag/"]')

    if hashtags:
        for hashtag in hashtags:
            print(hashtag.text)
    else:
        print("No hashtags found on this TikTok video.")
else:
    print("Failed to retrieve the TikTok video page.")
