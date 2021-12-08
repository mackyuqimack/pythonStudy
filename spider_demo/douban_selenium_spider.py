from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "https://movie.douban.com/top250?start=0&filter="
chromedriver_path = Service("D:/software/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=chromedriver_path)
driver.maximize_window()
film_info_list = []


def get_page_info():
    # 排名列表
    num_list = []
    # 标题列表
    title_list = []
    # 评分列表
    score_list = []
    # 详情列表
    detail_list = []
    hd_list = driver.find_elements(By.CLASS_NAME, "hd")
    for i in hd_list:
        title_list.append(i.find_element(By.CLASS_NAME, "title").text)
    bd_list = driver.find_element(By.CLASS_NAME, "grid_view").find_elements(By.CLASS_NAME, "bd")
    for i in bd_list:
        score_list.append(i.find_element(By.CLASS_NAME, "rating_num").text)
        try:
            detail_split = i.find_element(By.TAG_NAME, "p").text.split("\n")
            detail_list.append(detail_split[0].strip() + detail_split[1].strip())
        except:
            continue
    item_list = driver.find_elements(By.CLASS_NAME, "item")
    for i in item_list:
        num_list.append(i.find_element(By.TAG_NAME, "em").text)
    global film_info_list
    film_info_list += list(zip(num_list, title_list, score_list, detail_list))


def is_element_exist(element, name):
    """
    用来判断元素是否存在
    :param element:
    :return:
    """
    flag = True
    try:
        element.find_element(By.CSS_SELECTOR, name)
    except:
        flag = False
    return flag


def main():
    driver.get(path)
    get_page_info()
    # 翻页
    flag = True
    while flag:
        flag = is_element_exist(driver.find_element(By.CLASS_NAME, "next"), "a")
        print("正在执行第", driver.find_element(By.CLASS_NAME, "thispage").text, "页")
        driver.find_element(By.CLASS_NAME, "next").click()
        get_page_info()
    driver.quit()
    for num, title, score, detail in film_info_list:
        print(f"第{num}名为{title}，评分为{score}，详情为{detail}")


if __name__ == '__main__':
    main()
