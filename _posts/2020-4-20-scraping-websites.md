---
title: Scraping websites
date: 2020-4-20
categories: [scraping, selenium, beautifulsoup]

---

I want to scrape Netflix. I want that for several reasons. One of them is that I want to be able to play around with the recommendations, another one is that I want to make a mashup with IMDB data.

So, how to do it?

I am using Selenium, because I need to login to the site, and BeautifulSoup, so I can find elements in the DOM.
Here's my code so far: 

    import time
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import requests
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    
    driver.get ('https://www.netflix.com/nl-en/login')
    time.sleep(1)  # Let the user actually see something!
    driver.find_element_by_id('id_userLoginId').send_keys('my-e-mail-address')
    driver.find_element_by_id('id_password').send_keys('my-password')
    driver.find_element_by_css_selector(".login-button").click()
    time.sleep(1)  # Let the user actually see something!
    driver.find_element_by_link_text('Wijnand Baretta').click()
    time.sleep(1)  # Let the user actually see something!
    driver.find_element_by_link_text('Films').click()
    time.sleep(1)  # Let the user actually see something!
    # I am selecting the genre "Dutch Films"
    # The "?so=az" makes the ordering alphabetically 
    driver.get('https://www.netflix.com/browse/genre/10606?so=su')
    time.sleep(10)  # Quite a long wait to make sure the page is fully loaded

So now I am ready to start looking at the content of the page.

I managed to get all the movielinks and I want to include the titles as well as the image that goes with the movie.

The next step is to get the categories per movie. There are two approaches I'm considering:
- follow the link per movie and scrape all the content I want, including the categories.
- look up the movies per category, resulting in a movie_id/category_id pair.

I prefer the last method, for the simple reason that I will have the data in a format I can immediately store in a table.

Considering the load: I will have to go through all the categories I know (211)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAxMzYzNzE1NywtMTk4MDkxMjQwLC0xMj
U5MzA0Njc1LDE3NDM4ODMyNDcsLTgyNTU3MDczNSwxNzY2NzAy
MzcxLC0xMTQ5NDU4MzUzLDQ1MTYzODkyNCwtMTE2Nzg0MTM2OV
19
-->