import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
url = "https://movie.douban.com/top250?start=0&filter="
film_info_list = []


def get_total_page():
    """
    获取总页数
    """
    resp = requests.get(url=url, headers=headers)
    html = BeautifulSoup(resp.text, 'html.parser')
    return int(html.find("span", class_="next").previous_sibling.previous_sibling.text)


def get_title(html):
    """
    获取标题
    """
    title_list = html.find_all("div", class_="hd")
    for i in title_list:
        yield i.a.span.text


def get_score(html):
    """
    获取评分
    """
    star_list = html.find_all("div", class_="star")
    for i in star_list:
        yield i.find(class_="rating_num").text


def get_detail(html):
    """
    获取详情
    """
    detail_list = html.find_all("div", class_="bd")
    for i in detail_list:
        # yield fr"{i.p.text}".strip()
        try:
            yield i.p.text.split('\n')[1].strip() + i.p.text.split('\n')[2].strip()
        except:
            continue


def get_num(html):
    """
    获取排名
    """
    num_list = html.find_all("div", class_="pic")
    for i in num_list:
        yield i.em.text


def to_excel(data):
    """
    存入excel
    """
    import openpyxl
    wb = openpyxl.Workbook()
    wb.guess_type = True
    ws = wb.active
    ws.append(["排名", "电影名称", "评分", "详情"])
    for i in data:
        ws.append(i)
    wb.save("豆瓣top250电影排行榜.xlsx")


def main():
    total_page = get_total_page()
    global film_info_list
    for i in range(total_page):
        url_i = f"https://movie.douban.com/top250?start={i * 25}&filter="
        resp = requests.get(url=url_i, headers=headers)
        html = BeautifulSoup(resp.text, 'html.parser').find(class_="grid_view")
        num_list = get_num(html)
        title_list = get_title(html)
        score_list = get_score(html)
        detail_list = get_detail(html)
        film_info_list += list(zip(num_list, title_list, score_list, detail_list))
    # to_excel(film_info_list)
    for num, title, score, detail in film_info_list:
        print(f"第{num}名为{title}，评分为{score}，详情为{detail}")


if __name__ == '__main__':
    main()
