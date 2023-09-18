# "requests" helps us request the information of the targeting html.
# "BeautifulSoup" in "bs4" helps us parser requested html.
import requests
from bs4 import BeautifulSoup
# The following "headers" command helps us pretend to be a normal browser, instead of a crawler, so that
# the targeting html won't block our requests.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
# The information we need are likely stored in a html under many pages. The first for loop is to allow us read all pages of the targeting html.
for start_num in range(0, 250, 25):
# I actually not sure what exactly does the "f" do in the following line.
# The video says this "f" helps us 格式化. I don't quite understand.
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
# The following if statement helps us recognize if our request is succesful.
    if response.status_code >= 200 and response.status_code < 400:
        print("请求成功")
    elif response.status_code >= 400 and response.status_code < 500:
        print("请求失败，客户端错误")
    else:
        print("请求失败，服务器错误")
    print(response)
    print(response.status_code)
# We store all text information of this html as "html"
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
# We need to go back to the targeting website to find the locations of the information we want to find.
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)
# What's next? Learn how to store the above printed targeting information into an excel file.



