---
title: Scraping websites
date: 2020-4-20
categories: [scraping, selenium, beautifulsoup]

---

I want to scrape Netflix. I want that for several reasons. One of them is that I want to be able to play around with the recommendations, another one is that I want to make a mashup with IMDB data.

So, how to do it?

I am using Selenium, because I need to login to the site, and BeautifulSoup, . 

    import time
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import requests
    
 So these are the imports. Next, I need to use the webdriver. I am using Chrome. To locate it on a Linux machine, type
 

    whereis

 
    
    driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
    
      
      
    
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
    
    driver.get('https://www.netflix.com/browse/genre/10606?so=su')
    
    time.sleep(30)  # Let the user actually see something!

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzYyNDQ4M119
-->