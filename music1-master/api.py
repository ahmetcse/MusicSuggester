from bs4 import BeautifulSoup
import requests
from tools.regex import to_english


def getTrack(song_name):
    song_name = to_english(song_name)
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = f"https://soundcloud.com/search/sounds?q={song_name}"
    get = requests.get(url, headers=header)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find_all("ul", class_="")
    data = []
    for row in rows:
        temp = row.find_all("li", class_="")
        for song in temp:
            path = song.find("a", class_="")
            temp2 = song.text.strip()
            data.append({"link": path.get("href"), "title": temp2})

    return data[4:]
