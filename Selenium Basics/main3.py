from selenium import webdriver
from selenium.webdriver.common.by import By



# To keep chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.python.org/")

upcomming_events = driver.find_element(By.CSS_SELECTOR,value='.medium-widget.event-widget.last')

events_list = upcomming_events.find_elements(By.CSS_SELECTOR, value='ul.menu li')

events_dict = {}

for index, event in enumerate(events_list):


    event = event.text.split('\n')
    
    
    # We use .strip() just in case there are extra spaces
    event_date = event[0].strip()
    event_name = event[1].strip()
    
    # Construct the inner dictionary
    event_details = {
        'time': event_date,
        'name': event_name
    }
    
    events_dict[index] = event_details


print(events_dict)


driver.quit()