#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/23 9:54 
# @Author : TETE
# @File : test_fixture_param.py
import sys
import reason
import pytest
# test_user_data = ['Tom','Lily']
# # @pytest.fixture(params=[1,2,3,'linda'])
# # def test_data(request):
# #     return request.param
# #
# # def test_one(test_data):
# #     print('\ntest.data: %s'% test_data)
# @pytest.fixture(scope="module")
# def login_r(request):
#     user = request.param
#     print(f"\n 打开首页准备登录，登录用户：{user}")
#     return user
# @pytest.mark.xfail(reason='该功能尚未完善')
# # @pytest.mark.skip(sys.platform == 'darwin',reason="不在macos上执行")
# @pytest.mark.parametrize("login_r",test_user_data,indirect=True)
# def test_login(login_r):
#     a = login_r
#     print(f"测试用例中login 的返回值：{a}")
#     assert a != ''


class Test_Pytest():

        def test_one(self,):
                print("----start------")
                pytest.xfail(reason='该功能尚未完成')
                print("test_one方法执行" )
                assert 1==1

        def test_two(self):
                print("test_two方法执行" )
                assert "o" in "love"

        def test_three(self):
                print("test_three方法执行" )
                assert 3-2==1

if __name__=="__main__":
    pytest.main(['-s','-r','test_Pytest.py','test_Pytest.py'])