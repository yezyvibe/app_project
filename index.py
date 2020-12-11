from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests  

# response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
# with urlopen('https://www.naver.com/') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.select('span'):
#         print(anchor)

# 네이버 실시간 검색어 크롤링
json = requests.get('https://www.naver.com/srchrank?frm=main').json()
ranks = json.get('data')
file = open("새파일.txt", 'w')
for rank in ranks:
    r = str(rank.get('rank')) + '위 '
    keyword = rank.get('keyword')
    # print(r + keyword)
    data = r + keyword + "\n"
    file.write(data)
file.close()