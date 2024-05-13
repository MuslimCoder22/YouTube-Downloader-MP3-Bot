async def youtube(link):
    import requests
    import json

    url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "YOUR API KEY",
        "X-RapidAPI-Host": "youtube-mp3-downloader2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    audio = data['dlink']

    return audio


