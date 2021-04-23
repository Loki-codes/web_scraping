


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



def srape_image_url():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    relative_image_path= soup.find("img", class_="headerimage fade-in")["src"]
    mars_image_url = url + "/" + relative_image_path
    print(mars_image_url)

    # Quit the browser
    browser.quit()

    return mars_image_url


