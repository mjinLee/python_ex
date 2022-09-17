websites = ("google.com", "https://naver.com", "youtube.com", "https://kakaocorp.com")

for each in websites:
    print("hi")  # websites의 item 개수만큼 hi 출력

for echo in websites:
    print("echo is equals to", echo)
    print(echo)

for website in websites:
    if website.startswith("https://"):
        print("good to go")
    else:
        print("we have to fix it")

for website in websites:
    # if website.startswith("https://")==False:
    if not website.startswith("https://"):
        # print("have to fix")
        # string 안에 변수 넣기
        website = f"https://{website}"
    print(website)
