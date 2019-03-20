import requests
from flask import request
from bs4 import BeautifulSoup
import pandas as pd
import json
from flask import jsonify 

def nyJson():
    param = request.args.get('category', default = 'technology', type = str)
    url = "https://www.nytimes.com/section/%s"%param
    gethtml = requests.get(url)
    html = gethtml.text
    bs = BeautifulSoup(html, "lxml")
    news_list = bs.findAll('li',{'class':'css-ye6x8s'})
    df = pd.DataFrame(columns=['title','text','writer','news_link'])
    for i in news_list:
        title = i.find('h2',{'class':'css-1dq8tca'})
        text = i.find('p',{'class':'e1xfvim31'})
        writer = i.find('span',{'class':'css-1n7hynb'})
        link = i.find('a', href=True) 
        a_link = link['href']
        news_link = "https://www.nytimes.com/%s"%a_link
        title = title.text.strip()
        text = text.text.strip()
        writer = writer.text.strip()
        lists = [title,text,writer,news_link]
        a = pd.DataFrame([lists],columns=['title','text','writer','news_link'])
        df = df.append(a)
    json_output = json.loads(df.to_json(orient='records'))
    return jsonify(json_output)

def contentGetter():
    param = request.args.get('category', default = 'technology', type = str)
    url = "https://www.nytimes.com/section/%s"%param
    gethtml = requests.get(url)
    html = gethtml.text
    bs = BeautifulSoup(html, "lxml")
    news_list = bs.findAll('li',{'class':'css-ye6x8s'})
    df = pd.DataFrame(columns=['title','text','writer','link','content'])
    for i in news_list:
        title = i.find('h2',{'class':'css-1dq8tca'})
        text = i.find('p',{'class':'e1xfvim31'})
        writer = i.find('span',{'class':'css-1n7hynb'})
        title = title.text.strip()
        text = text.text.strip()
        writer = writer.text.strip()
        link = i.find('a', href=True) 
        a_link = link['href']
        full_link = "https://www.nytimes.com/%s"%a_link
        gethtml = requests.get(full_link)
        html = gethtml.text
        bs = BeautifulSoup(html, "lxml")
        content = bs.find('section',{'class':'css-1i2y565'}) 
        content_text = content.findAll('p',{'class':'evys1bk0'})
        content_list = []
        for i in content_text:
            content_list.append(i.text.strip())
        content = ' '.join(content_list) 
        lists = [title,text,writer,full_link,content]
        a = pd.DataFrame([lists],columns=['title','text','writer','link','content'])
        df = df.append(a)
    json_output = json.loads(df.to_json(orient='records'))
    return jsonify(json_output)