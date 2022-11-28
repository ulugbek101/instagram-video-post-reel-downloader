import requests


def get_response(unknown_link: str) -> requests.Response | None:
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
    querystring = {"url": f"{unknown_link}"}
    headers = {
        "X-RapidAPI-Key": "61c70485b7msh59d85911958a368p1d646djsn4eaeaef4ef3d",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    try:
        response.raise_for_status()
        return response
    except:
        return None
