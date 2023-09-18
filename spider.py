# "requests" helps us request the information of the targeting html.
# "BeautifulSoup" in "bs4" helps us parser requested html.
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# The following "headers" command helps us pretend to be a normal browser, instead of a crawler, so that
# the targeting html won't block our requests.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
# I actually not sure what exactly does the "f" do in the following line.
# The video says this "f" helps us 格式化. I don't quite understand.
response = requests.get("http://guba.eastmoney.com/list,300897,99.html", headers=headers)
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
#print(html)
soup = BeautifulSoup(html, "html.parser")
# We need to go back to the targeting website to find the locations of the information we want to find.
comments=[]
all_comments = soup.findAll("div", attrs={"class": "title"})
for content in all_comments:
 #   print(content)
    content_string = content.string
    comments.append(content_string)
# print(comments)
# print(len(comments))

authors = []
all_authors = soup.findAll("div", attrs={"class": "author cl"})
for author in all_authors:
    print(author)


## Store the above printed targeting information into an excel file!
# data = {'Comments':comments}
# df=pd.DataFrame(data)
# df.to_excel("/Users/zwang/Documents/Research/motivation_text_sentiment/text_sentiment_analysis/output.xlsx", sheet_name='Sheet1', startrow=0, startcol=0)

