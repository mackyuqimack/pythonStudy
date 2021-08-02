from selenium import webdriver

path = "https://movie.douban.com/top250?start=0&filter="
chromedriver_path = "D:/software/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)
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
    hd_list = driver.find_elements_by_class_name("hd")
    for i in hd_list:
        title_list.append(i.find_element_by_class_name("title").text)
    bd_list = driver.find_element_by_class_name("grid_view").find_elements_by_class_name("bd")
    for i in bd_list:
        score_list.append(i.find_element_by_class_name("rating_num").text)
        try:
            detail_split = i.find_element_by_tag_name("p").text.split("\n")
            detail_list.append(detail_split[0].strip() + detail_split[1].strip())
        except:
            continue
    item_list = driver.find_elements_by_class_name("item")
    for i in item_list:
        num_list.append(i.find_element_by_tag_name("em").text)
    global film_info_list
    film_info_list += list(zip(num_list, title_list, score_list, detail_list))


def isElementExist(element, name):
    """
    用来判断元素是否存在
    :param element:
    :return:
    """
    flag = True
    try:
        element.find_element_by_css_selector(name)
    except:
        flag = False
    return flag


def main():
    driver.get(path)
    get_page_info()
    # 翻页
    flag = True
    while flag:
        flag = isElementExist(driver.find_element_by_class_name("next"), "a")
        print("正在执行第", driver.find_element_by_class_name("thispage").text, "页")
        driver.find_element_by_class_name("next").click()
        get_page_info()
    driver.quit()
    for num, title, score, detail in film_info_list:
        print(f"第{num}名为{title}，评分为{score}，详情为{detail}")


if __name__ == '__main__':
    main()
