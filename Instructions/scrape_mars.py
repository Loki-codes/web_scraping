import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import time
from pprint import pprint
import requests
import pymongo
from mars_image_scraper import srape_image_url
from mars_news_scraper import scrape_news
from mars_scrape_hemi import hemi_image_link_maker
from mars_table_scraper import scrape_table

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db
collection = db.info

data = []
info = {}
def scrape():
    data.append(srape_image_url())
    data.append(scrape_news())
    data.append(hemi_image_link_maker())
    data.append(scrape_table())

    info = {
        'pop_image' : data[0],
        "news" : data[1],
        "hemi_pics" : data[2],
        "table" : data[3]
    }
    
    collection.insert_one(info)

    return info




