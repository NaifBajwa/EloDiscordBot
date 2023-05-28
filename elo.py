import requests
from bs4 import BeautifulSoup
import re

class OmedaCityWeb:
  def __init__(self):
      self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
      self.url = 'https://omeda.city/search?sq='

  '''def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words'''

  def search(self, keywords):
    response = requests.get(self.url+keywords, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    #result_links = soup.findAll('a')
    #mydivs = soup.findAll('div')
    mydivs = soup.find("div",{"class":"search-stats"}).get_text()
    winrateDiv = soup.find("div",{"class":"progress-bar"})
    winrate = winrateDiv["style"].split("width: ")
    print (winrate)
    mydivs = re.sub(r"[\t]*", "", mydivs)
    list = mydivs.split(" ")
    list = [x for x in list if x != '']
    delimiter = ''
    joinList = delimiter.join(list)
    list = joinList.split("\n")
    list = [x for x in list if x != '']
      
    print(list)
    customMMR = list[0]+' '+list[1]+'\n'+list[2]+' '+list[3]+'\n'+list[4]+': '+winrate[1]+'\n'+list[5]+' '+list[6]
    #for div in mydivs: 
      #if (div["class"] == "search-stat"):
    print (customMMR)
    #print ("new div")
    return customMMR
      
  '''def send_link(self, result_links, search_words): 
    send_link = set()
    for link in result_links:
        text = link.text.lower()
        if search_words in text:  
          send_link.add(link.get('href'))
    return send_link'''