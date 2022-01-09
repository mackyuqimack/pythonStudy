# coding=utf-8
def main():
    read_excel("1.xlsx")


def read_excel(url):
    """
    读取excel方法
    :param url: excel路径
    :return:
    """
    import openpyxl
    wb = openpyxl.load_workbook(url)
    # 获取所有工作表名
    names = wb.sheetnames
    sheet = wb[names[0]]
    cell = sheet.rows
    msg = ""
    for i in cell:
        if i[0].value == '标题':
            continue
        print(i[0].value, i[1].value)
        msg += i[0].value + i[1].value
    write_file(msg)


def write_file(data):
    """
    写入文件方法
    :param data: 内容
    :return:
    """
    with open("insert.txt", "w") as f:
        f.write(data)


if __name__ == '__main__':
    main()
