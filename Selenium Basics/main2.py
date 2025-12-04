from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")





search_bar = driver.find_element(By.NAME,value='q')

print(search_bar)
print()
print(search_bar.tag_name)
print()
print(search_bar.get_attribute('placeholder'))



# Finding Element by ID

Button = driver.find_element(By.ID,value='submit')
print(Button.size)



# Finding Element by CSS Selector

# We use additional dot for spaces in class named
# In the below the class is "small-widget documentation-widget" and
# we are trying to find an achor tag withing that class element.
documentation__link = driver.find_element(By.CSS_SELECTOR,value='.small-widget.documentation-widget a')
print(documentation__link.text)
print()




# Using Xpath to find a an element
bug_link = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)





driver.quit()