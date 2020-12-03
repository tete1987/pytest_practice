#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/24 14:04 
# @Author : TETE
# @File : test_allure_login.py
import pytest
import allure

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_failure(self):
        print("这是登录：测试用例，登录失败")
        pass

    @allure.story("用户名缺失")
    def test_login_fail_a(self):
        with allure.step("点击用户名"):
            print("请输入用户名")
        with allure.step("点击密码"):
            print("请输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' ==1
            print("密码不正确，登录失败")


    @allure.story("密码缺失")
    def test_login_fail_b(self):
        print("密码缺失")
        pass

if __name__ == '__main__':
    pytest.main()