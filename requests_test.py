# import requests
from tkinter import W
from unittest import result
from requests import get

websites = ("google.com", "https://naver.com", "youtube.com", "https://kakaocorp.com")

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    # print(website)
    response = get(website).status_code
    # print(response)  # <Response [200]>
    # print(response.status_code)  # 200
    if response >= 100 and response < 200:
        results[website] = "continue"
    elif response >= 200 and response < 300:
        # print(f"{website} is ok")
        results[website] = "success"
    elif response >= 300 and response < 400:
        results[website] = "redirection"
    elif response >= 400 and response < 500:
        results[website] = "client error"
    elif response >= 500 and response < 600:
        results[website] = "server error"
    else:
        # print(f"{website} is not ok")
        results[website] = "FAILED"
print(results)
