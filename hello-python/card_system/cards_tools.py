# 记录所有的名片字段
card_list = []


def show_menu():

    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print()
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print()
    print("0. 退出系统")
    print("*" * 50)


def new_card():

    """新增名片"""
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名: ")
    phone_str = input("请输入电话号码: ")
    qq_str = input("请输入QQ: ")
    email_str = input("请输入Email: ")
    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)
    # 4. 提示用户输入成功
    print("添加%s成功" % name_str)


def show_all():

    """显示所有名片"""
    print("显示全部名片")
    for card in card_list:
        print(card)


def search_card():

    """搜索名片"""
    print("搜索名片")
    index = int(input("请输入查询编号："))
    print(card_list[index])