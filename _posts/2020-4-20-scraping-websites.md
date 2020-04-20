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
    # The "?so=su"  
    driver.get('https://www.netflix.com/browse/genre/10606?so=su')
    time.sleep(10)  # Quite a long wait to make sure the page is fully loaded

So now I am ready to gstart looking at the content of the page.

<!--stackedit_data:
eyJoaXN0b3J5IjpbNDUxNjM4OTI0LC0xMTY3ODQxMzY5XX0=
-->