import time
import csv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

driver = Chrome('C:\\Users\\rholl\\Documents\\ChromeDriver\\chromedriver')
path = 'C:\\Users\\rholl\\Desktop\\random_stats.csv'
file = open(path, 'r', newline='')
reader = csv.reader(file, delimiter=',')
next(reader)
data = []
for data in reader:
    random_stats = data[0]
    print(random_stats)

    while True:
        try:
            driver.get('https://www.bing.com')
            time.sleep(2)
            search_box = driver.find_element_by_id('sb_form_q')
            time.sleep(2)
            search_box.send_keys(random_stats)
            time.sleep(2)
            search_box.submit()
            images = driver.find_element_by_xpath("//*[@id='b_header']/nav/ul/li[2]/a")
            images.click()
            time.sleep(5)
        except NoSuchElementException:
            driver.get('https://www.bing.com')
            pass
        else:
            pass
        finally:
            break
time.sleep(5)
driver.quit()
