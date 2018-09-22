# Imports
import time
from splinter import Browser
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
# Mission to Mars - scraping function
def init_browser():
    # Initialize Chromedriver path
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
     # Initialize dictionary to store return values
    mars_portal_info = {}

    # Initialize browser that we can re-use
    browser = init_browser()

    # *** 1. Obtain News headline and description ***
    # Define URL to scrape first - Mars News site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Wait for page to load
    time.sleep(2)

    # Pass the HTML output from the splinter session
    html = browser.html  
    soup = bs(html, 'html.parser')

    # Collect latest News title and paragraph text
    news_title = soup.select('.grid_gallery.list_view li.slide .content_title a', limit=1)[0].contents[0]
    news_p = soup.select('.grid_gallery.list_view li.slide .article_teaser_body', limit=1)[0].contents[0]

    # Add to return value dictionary
    mars_portal_info["news_title"] = news_title
    mars_portal_info["news_description"] = news_p
    print(news_p)

    #
    # *** 2. Grab featured Mars image from Cal Tech Jet propulsion lab home page ***
    #
    url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_jpl)

    # Wait for page to load
    time.sleep(2)

    # Pass the HTML output from the splinter session
    html = browser.html  
    soup = bs(html, 'html.parser')

    # Parse the featured image from the HTML
    featured_image_relative_path = soup.select('div.carousel_container .floating_text_area footer a')[0]["data-fancybox-href"]
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image_relative_path}"

    # Add to return value dictionary
    mars_portal_info["featured_image_url"] = featured_image_url
    print(featured_image_url)

    #
    # *** 3. Scrape the latest Mars weather tweet from the Mars weather Twitter page ***
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    # Wait for page to load
    time.sleep(2)

    # Pass the HTML output from the splinter session
    html = browser.html  
    soup = bs(html, 'html.parser')

    # Find all tweets on the page
    all_tweets = soup.select('.stream-items .js-stream-item .tweet .content p')

    # Loop through tweets to get the first actual weather report
    mars_weather = ""
    for result in all_tweets:
        tweet_text = result.contents[0]
        tweet_first_three = tweet_text[0:3]
        if tweet_first_three == 'Sol':
            mars_weather = tweet_text
            break

    # Add to return value dictionary
    mars_portal_info["mars_weather"] = mars_weather
    print(mars_weather)

    # *** 4. Scrape Mars facts table from https://space-facts.com/mars/ ***
    #tps://space-facts.com/mars/"
    # Bring table into Pandas
    tables = pd.read_html(facts_url)
    df = tables[0]

    # Export dataframe to HTML string
    mars_facts_table = df.to_html(buf=None, columns=None, col_space=None, header=False, index=False, \
                    na_rep='NaN', index_names=False, justify='right', bold_rows=True, classes=None, \
                    escape=True, max_rows=None, max_cols=None, show_dimensions=False, \
                    notebook=False, decimal='.', border=1)
    mars_portal_info["mars_facts_table"] = mars_facts_table

    # Return dictionary of scraped values we created
    return mars_portal_info

def test():
    return {
        "news_title": "Really Cool Title here",
        "news_description": "NASA's next mission to Mars passed a key test Tuesday, extending the solar arrays that will power the InSight spacecraft once it lands on the Red Planet this November.",
        "featured_image_url": "http://lorempixel.com/g/400/200/", 
        "mars_weather": "Sol 1942 (Jan 22, 2018), Sunny, high -27C/-16F, low -78C/-108F, pressure at 7.57 hPa, daylight 05:44-17:29",
        "mars_facts_table": "<table><tr><td>Cool fact 1</td><td>Fact fact fact fact fact</td></tr><tr><td>Cool fact 1</td><td>Fact fact fact fact fact</td></tr><tr><td>Cool fact 1</td><td>Fact fact fact fact fact</td></tr><tr><td>Cool fact 1</td><td>Fact fact fact fact fact</td></tr><tr><td>Cool fact 1</td><td>Fact fact fact fact fact</td></tr></table>"
    }
# For debugging purposes only - when we run 'python scrape_mars.py'
if __name__ == "__main__":
    scrape()