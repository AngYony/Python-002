import requests
from bs4 import BeautifulSoup as bs
import codecs
url = 'https://maoyan.com/films?showType=3'

header = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'uuid_n_v=v1; uuid=A284D330CFDC11EA982967E84AE799F97C71E92BCFB94283A850AB83C2FD44AF; _csrf=99ac6c542ba8e83b6ddd6c1cd4ff0c4d23f8fd5bb03e38ade7dbb816b54eb37b; mojo-uuid=87bbf0dbaaa811972843043917b2b132; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595835713; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595835713; _lxsdk_cuid=1738f3885d8c8-09538aa9f81dc9-5d37194b-1fa400-1738f3885d8c8; _lxsdk=A284D330CFDC11EA982967E84AE799F97C71E92BCFB94283A850AB83C2FD44AF; mojo-session-id={"id":"662e53534754836449047f317f00ddf7","time":1595835713005}; mojo-trace-id=1; __mta=174413085.1595835713274.1595835713274.1595835713274.1; _lxsdk_s=1738f3885d9-b35-789-a9b%7C%7C2'

}

response = requests.get(url, headers=header)

 
response.encoding = response.apparent_encoding
codecs.open('D://maoyan.html', "w", "utf-8").write(response.text)

# 将输出的结果保存



bs_info = bs(response.text, 'html.parser')

wy = bs_info.find('dl', attrs={'class': 'movie-list'})
print(wy)




# for tags in movie_list.find_all('div', attrs={'class': 'movie-hover-info'},limit=10):
#     print(tags)
# for atag in tags.find_all('div',attrs={'class': 'movie-hover-title'}):
#     print(atag.find('span',attrs={'class': 'name '}).text)
