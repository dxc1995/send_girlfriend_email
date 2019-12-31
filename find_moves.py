import requests
from bs4 import BeautifulSoup

"""
  爬取猫眼最新上映电影
"""
# 请求猫眼地址
def open_url(url):
    # 浏览器伪装
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url, headers=headers)
    return response

def find_movies(res):
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 电影名
    movies = []
    targets = soup.find_all("div", class_="channel-detail movie-item-title")
    for each in targets:
        movies.append(each.a.text)
    
    # 评分
    ranks = []
    targets  = soup.find_all("div", class_="channel-detail channel-detail-orange")
    for each in targets:
        ranks.append("评分:%s"% each.text)
    
    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + "\t" + ranks[i] + "\t")
    return result

def main():
    host = "https://maoyan.com/films?yearId=14&showType=1&sortId=2"
    res  = open_url(host)
    
    movies_list = []
    movies_list.extend(find_movies(res))

    with open("猫眼电影最近上映.txt", "w", encoding="utf-8") as f:
        for each in movies_list:
            f.writelines(each + "\n")

main()








