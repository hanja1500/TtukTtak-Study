from bs4 import BeautifulSoup
import requests, re, os
import urllib.request

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

dirto = input("[*] input directory name you want to download webtoon > ")
try:
    if not (os.path.isdir(dirto)):
        os.makedirs(os.path.join(dirto))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("[!] failed to make directory!")
        exit()

html = requests.get("https://comic.naver.com/webtoon/detail?titleId=738809&no=101&weekday=mon")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

img_div = soup.find("div", {"class", "wt_viewer"})
img_all = img_div.findAll("img")

num = 1
for j in img_all:
    img_path = j.get("src")
    img_num = "./webtoon/"+str(num)+".jpg"
    urllib.request.urlretrieve(img_path, img_num)
    num += 1

print("[*] success to download the webtoon file!")
