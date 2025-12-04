from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.de/-/en/Instant-IP-DUO60-Programmable-Electric-Pressure/dp/B08Z4HCGDH/ref=sr_1_1?crid=304BC9VQ4CDAM&dib=eyJ2IjoiMSJ9.J2chGoDwqurz7IE-xaFOXIIqX992tHnvpEYXGr9QMOPCj_w847enj5xI1TkTUcdSzoyHYvZom7aJe3bSq2E1EOtsZukjIhDkG8kBmngPq-Ch1twPdJT0Pv7nYDCgkIQ1eaCN9b5vcmyA8xTeHy68FJ1t9zYKJ-7HNazEaWoWmcZ_cf_K0GRFnzyBo52KeGMhDIcggSKODzy7skVQWnQdCvcxUWyUrAnBb_R-mn8GIb8.rnI6dA4FKG4hY1hckREVMFPfh9ZSzhxzJIUch5iQpAY&dib_tag=se&keywords=instant%2Bpot%2Bduo&qid=1764838479&sprefix=instant%2Bpot%2Bduo%2Caps%2C134&sr=8-1&th=1")


price_euro = driver.find_element(By.CLASS_NAME,value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME,value='a-price-fraction')
print(f'The price is {price_euro}.{price_cents}')


driver.quit()