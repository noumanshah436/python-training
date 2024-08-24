def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.spVoice")
    speak.Speak(str)


if __name__ == "__main__":
    import requests
    import json

    url = (
        "https://newsapi.org/v2/top-headlines?"
        "sources=bbc-sport&"
        "apiKey=23bbe0a14a804131896e3c0bb7874061"
    )

    response = requests.get(url)
    text = response.text
    print(text)
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json["articles"][i]["title"])
