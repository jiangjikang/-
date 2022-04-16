# -*- coding: UTF-8 -*-
"""
@Project ：pythonProject 
@File    ：cards_main.py
@Author  ：Jiang
@Date    ：2021/11/27 21:18 
"""
from cards_tool import *


def main():
    if Id.names == Id.name and Id.passwords == Id.password:

        while True:
            # TODO(蒋继康) 显示菜单
            show_menu()
            action_str = input("请输入要操纵的数字：")
            print("你选择的操纵是【%s】" % action_str)
            if action_str in ["1", "2", "3"]:
                if action_str == "1":
                    new_card()
                elif action_str == "2":
                    show_all()
                elif action_str == "3":
                    search_card()
            elif action_str == "0":
                print("程序已退出")
                break
            else:
                print("你输入的不正确！请重新输入")
    else:
        print("密码或用户名错误！")
        name = input("找回密码----是 OR 否")
        if name == "是":
            iphone = input("请输入邮箱：")


if __name__ == "__main__":
    main()
