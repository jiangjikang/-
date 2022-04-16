# -*- coding: UTF-8 -*-
"""
@Project ：pythonProject 
@File    ：cards_tool.py
@Author  ：Jiang
@Date    ：2021/11/27 21:18 
"""

card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 25)
    print("欢迎使用【名片管理系统】V1.0")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print("*" * 25)


def new_card():
    """添加名片"""
    print("-" * 25)
    print("新增名片")
    name_str = input("请输入姓名：")
    age_str = int(input("请输入年龄:"))
    phone_str = int(input("请输入电话号码:"))
    email_str = input("请输入邮箱:")
    card_dict = {
        "name": name_str,
        "age": age_str,
        "phone": phone_str,
        "email": email_str,
    }
    card_list.append(card_dict)
    print("添加%s名片成功！" % name_str)


class Id:
    name = 'Jiang'
    passwords = "jiang."
    names = input("请输入用户名：")
    password = input("请输入密码：")


def show_all():
    """显示名片"""
    if len(card_list) == 0:
        print("当前没有任何名片")
        return
    print("-" * 50)
    print("显示所有名片")
    for name in ["姓名", "年龄", "电话", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)

    for card_dict in card_list:
        print(
            "%s\t\t%s\t\t%s\t\t%s\t\t" % (
                card_dict["name"], card_dict["age"], card_dict["phone"], card_dict["email"]))


def search_card():
    """查询名片"""
    print("-" * 50)
    print("搜索名片")
    consult = input("请输入要查询的名片：")
    for card_dict in card_list:
        if card_dict["name"] == consult:
            print("姓名\t\t年龄\t\t电话\t\t邮箱")
            print("=" * 50)
            print(
                "%s\t\t%s\t\t%s\t\t%s\t\t" % (
                    card_dict["name"], card_dict["age"], card_dict["phone"], card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到%s" % consult)


def deal_card(find_card):
    action_str = input("请输入要执行的操纵："
                       "【1】：修改  【2】：删除  【0】：返回上一级")
    if action_str == "1":
        # 修改名片
        find_card["name"] = input_card_info(find_card["name"], "姓名：")
        find_card["age"] = input_card_info(find_card["age"], "年龄：")
        find_card["phone"] = input_card_info(find_card["phone"], "电话：")
        find_card["email"] = input_card_info(find_card["email"], "邮箱：")
        print("修改成功")
    elif action_str == "2":
        # 删除名片
        card_list.remove(find_card)
        print("删除成功")


def input_card_info(dict_value, tip_message):
    """输入名片信息
    :param dict_value:  字典中原有的值
    :param tip_message: 输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则就返回字典中 原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
