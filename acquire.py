import numpy as np
import pandas as pd
import os
from requests import get
from bs4 import BeautifulSoup as soupify

url1='https://codeup.com/featured/financing-career-transition/'
url2='https://codeup.com/codeup-news/dei-report/'
url3='https://codeup.com/codeup-news/diversity-and-inclusion-award/'
url4='https://codeup.com/tips-for-prospective-students/tips-for-women/'
url5='https://codeup.com/cloud-administration/cloud-computing-and-aws/'

articles=[url1,url2,url3,url4,url5]


headers = {'User-Agent': 'hackers anon'}

def get_blog_articles(url):
    """takes in url from codeup blog website and returns a dictionary with the 
    title as the key and the content as the value """
    soup=soupify(get(url,headers=headers).content, 'html.parser')
    
    header=soup.h1.text.strip()
    body=soup.find('div',{'class':'entry-content'}).text.strip()
    return {'title': header,'content': body}


url = 'https://inshorts.com/en/read'


def get_cats(base_url):
    soup = soupify(get(base_url).content)
    return [cat.text.lower() for cat in soup.find_all('li')[1:]]


def get_news_articles(base_url):
    """scrapes inshorts website and returns earch business, sports,
     technology, and entertainment news article and returns them in a list of dictionaries"""
    cats = get_cats(base_url)
    all_articles = []
    for cat in cats:
        cat_url = base_url + '/' + cat
        print(get(cat_url))
        cat_soup = soupify(get(cat_url).content)
        cat_titles = [
            title.text for title in cat_soup.find_all('span', itemprop='headline')
        ]
        cat_bodies = [
            body.text for body in cat_soup.find_all('div', itemprop='articleBody')]
        cat_articles = [{'title': title,
        'category': cat,
        'body': body} for title, body in zip(
        cat_titles, cat_bodies)]
        print('cat articles length: ',len(cat_articles))
        all_articles.extend(cat_articles)
        print('length of all_articles: ', len(all_articles))
    return all_articles