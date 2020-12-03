#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/23 9:38 
# @Author : TETE
# @File : test_yield.py
import pytest

@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")
    #在yield关键字后面的语句最后执行
    yield
    print("执行teardown")
    print("最后关闭浏览器")

def test_search(open):
    print("test_search")
    pass

def test_search2(login):
    print("test_search2")
    pass

if __name__ == "__main__":
    pytest.main()