from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import pyquery as pq
from config import *


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
browser.get(
    'https://www.tmall.com')
def search():
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mq"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mallSearch > form > fieldset > div > button"))
        )
        input.send_keys('美食')
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.ui-page > div > b.ui-page-skip > form"))
        )
        return total.text
    except Exception:
        return search()

def get_product():
    wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#J_ItemList .product .product-iWrap"))
        )
    html = browser.page_source
    doc = pq(html)
    items = doc('#J_ItemList .product .product-iWrap').items()
    print(items)
    for item in items:
        title = item.find('.pic.img').attr('src'),



def main():
    total =search()
    total =re.findall('\d+',total)
    page_nubmer = int(total[0])
    print(page_nubmer)
    session.add_all(list)





if __name__ == '__main__':
    main()

