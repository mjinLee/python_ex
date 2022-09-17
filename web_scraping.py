from requests import get
from bs4 import BeautifulSoup

# website get
base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    # print(response.text)  # response의 text(website's html code) 받아옴
    # beautifulsoup
    # webpage의 모든 html
    soup = BeautifulSoup(response.text, "html.parser")
    # job class를 가지고 있는 모든 section
    jobs = soup.find_all("section", class_="jobs")
    # print(len(jobs)) # 3개
    for job_section in jobs:
        job_posts = job_section.find_all("li")  # li
        # 가장 마지막에 있는 'view-all' li를 제외
        job_posts.pop(-1)
        for post in job_posts:
            print(post)
            print("//////////////")  # li 구분
