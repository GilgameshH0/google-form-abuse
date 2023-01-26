import requests
import time
from fake_useragent import UserAgent

k = 0

with open("twitter.txt") as file1, open("wallet.txt") as file3:
    for twitter, wallet in zip(file1, file3):
        k = k + 1
        ua = UserAgent()
        useragent = ua.random

        form_data = {'entry.1852888101': twitter.rstrip(), 'entry.1712836901': wallet.rstrip() }

        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': useragent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', "Referer":"https://docs.google.com/forms/d/e/1FAIpQLSf5QAhKbvMOq414UL6eF74KdhOFu5tpWBzYLZ5v7SgNh_XI2Q/viewform"} 
        
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSf5QAhKbvMOq414UL6eF74KdhOFu5tpWBzYLZ5v7SgNh_XI2Q/formResponse"
        request = requests.post(url=url, data=form_data, headers=headers)
        print(str(request.status_code) + " : " + str(k) + " : " + twitter.rstrip() + " : " + wallet.rstrip())
        time.sleep(1)