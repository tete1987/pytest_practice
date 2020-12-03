#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/25 8:58 
# @Author : TETE
# @File : test_allure_level.py
import allure
import pytest

class TestLevel():
    def test_no_lable(self):
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_trival(self):
        print("这是一个trivial类的测试用例")
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_critical(self):
        print("这是一个critical类的测试用例")
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_normal(self):
        print("这是一个normal类的测试用例")
        pass

if __name__ == '__main__':
    pytest.main()
