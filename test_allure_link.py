#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/24 16:48 
# @Author : TETE
# @File : test_allure_link.py
import allure

# @allure.link("http://192.168.124.149:31000/",name="万达项目")
# def test_with_link():
#     print("这是一条加了链接的测试")

# test_case_link = "http://192.168.124.149:31000"
# @allure.link(test_case_link,"test_case_title")
# def test_link():
#     print("这是一条测试用例的链接，链接到测试用例里面")
#     pass

#--allure-link-pattern=issur:http://192.168.124.120/zentao/issue/bug-view-4870.html
@allure.issue('4870','这是一个issue')
def test_issue():
    print("这是一个bug")
    pass
