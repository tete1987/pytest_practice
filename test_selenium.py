#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/25 10:32 
# @Author : TETE
# @File : test_selenium.py
import allure
import pytest
from selenium import webdriver
import time
import selenium

@allure.feature('百度搜索')
@pytest.mark.parametrize('data',['allure','test_case','pytest'])
def test_step_demo(data):
    with allure.step('打开百度'):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")

    with allure.step('输入关键词，并进行点击'):
        driver.find_element_by_id("kw").send_keys(data)
        time.sleep(1)
        driver.find_element_by_id("su").click()
        time.sleep(1)

    with allure.step('进行截图'):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页<body>",'Attach with HTML type',allure.attachment_type.HTML)

    with allure.step('关闭浏览器'):
        driver.quit()