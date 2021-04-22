#!/usr/bin/env python
# coding: utf-8

# In[59]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import time


# In[61]:


# I needed a list to hold the dictionary of resonses from this function as well as a variable to hold the
# chunks of html that I would need to click through. 
links = []
chunks = []
def hemi_image_link_maker():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
#     creating the chunks of html to loop through to go to each hemisphere's web page.
    chunks =soup.find_all("div" ,class_="item")
    for i in range(len(chunks)):
        hemi_page = browser.find_by_css("a.product-item h3")
        hemi_page[i].click()
        time.sleep(1)
        img_html = browser.html
        img_soup = BeautifulSoup(img_html,'html.parser')
#         get the title of the photo
        title = img_soup.find('h2', class_='title').get_text()
#         get the url of the photo
        img_page = img_soup.find('div', class_='downloads')
        img_box = img_page.find('li')
        img_link = img_box.find('a')['href']
        
        img_whole_link = f"{url}{img_link}"
        
        links.append({"title": title,
                    'Image_link': img_whole_link})
        browser.back()
        
        return links
   


# In[ ]:




