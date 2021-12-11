from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from util import driver

path = "https://www.baidu.com"
driver.check_update_chromedriver()
chromedriver_path = Service(driver.get_chromedriver_path())
driver = webdriver.Chrome(service=chromedriver_path)
driver.maximize_window()


def main():
    driver.get(path)
    # 登录
    driver.find_element(By.ID, "s-top-loginbtn").click()
    input('登陆后按Enter键继续...')
    name = driver.find_element(By.CLASS_NAME, "user-name").text
    print(name)
    driver.quit()


if __name__ == '__main__':
    main()
