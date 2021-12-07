from selenium import webdriver
from spider_demo import driver_util

path = "https://www.baidu.com"
driver_util.check_update_chromedriver()
chromedriver_path = driver_util.get_chromedriver_path()
driver = webdriver.Chrome(chromedriver_path)
driver.maximize_window()


def main():
    driver.get(path)
    # 登录
    driver.find_element_by_id("s-top-loginbtn").click()
    input('登陆后按Enter键继续...')
    name = driver.find_element_by_class_name("user-name").text
    print(name)
    driver.quit()


if __name__ == '__main__':
    main()
