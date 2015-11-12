import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import csv


def scrapSite(url):
    pageNumber = 1
    neighbours = []
    while True:
        currentURL = ''.join([url,str(pageNumber)])
        htmlText = requests.get(currentURL).text
        soup = BeautifulSoup(htmlText)

        followers = soup.find_all('div',class_ = 'user_strip')

        if len(followers) == 0: 
            parentName = soup.title.string.split('|')[0].strip()
            neighbours.append(parentName)
            neighbours.append(len(neighbours)-1)
            break        
        else:
            pageNumber +=1
            for i in followers:
                neighbours.append(i.find('a', attrs={"data-has-card-for-user": re.compile(u'\d+')})['href'])
    return neighbours

#scrapSite(url)


#def findHref(tag):
#    if tag.has_attr('data-has-card-for-user') and tag['class'] == 'user_strip clearfix':
#        #link = tag.Con('a')
#        return tag


def BFS():    
    #startNode = 'https://asu.academia.edu/HuanLiu' 
    startNode = 'http://asu.academia.edu/AravindKumarReddyYempada'
    neighbours=[]
    nodesScraped = []
    url = ''.join([startNode,'/Followers?_pjax=.center-column+>+.content&page='])
    depth = 0
    followers = scrapSite(url)
    neighbours.append(followers)
    nodesScraped.append(followers[-2])
    count = len(neighbours[depth])-2

    file = open('output2.csv','wb')
    wr =  csv.writer(file)
    wr.writerow(followers)


    while True:
        depth += 1
        flag = False
        for node in neighbours[depth-1][:-2]:
            if node[-2] not in nodesScraped:
                url = ''.join([node,'/Followers?_pjax=.center-column+>+.content&page='])
                followers = scrapSite(url)
                neighbours.append( followers)
                nodesScraped.append(followers[-2])
                wr.writerow(followers)
                count += len(neighbours[depth])-2
                if count > 25000 or len(neighbours[depth])==0: 
                    flag= True
                    break
        if flag: break

    file.close()

BFS()

