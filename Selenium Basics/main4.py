from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint


# To keep chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_stats = driver.find_element(By.ID,value='articlecount')


value = article_stats.find_elements(By.TAG_NAME,value='a')

print(value[1].text)



driver.quit()

