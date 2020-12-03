#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/20 15:20 
# @Author : TETE
# @File : test_pytest01.py
import pytest
from pytest_assume.plugin import assume
import pytest_assume
def setup_module():
    print("这是一个setup_module 方法")

def teardown_module():
    print("这是teardown_module 方法")

def setup_function():
    print("这是 setup_function 方法")

def teardown_function():
    print("这是 teardown_function 方法")

class TestDemo:
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    def teardown_class(self):
        print("teardown_class")

class Test01():
    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert "h" in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = "hello"
        assert "e" in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = "hello"
        b = "hello world"
        assert a  in b

    def test_four(self):
        print("开始执行 test_four 方法")
        a = "hello"
        b = "hello world"
        assert a in b

if __name__ == "__main__":
    pytest.main()
    #或者以下这种写法，均可
    # pytest.main(["-v", "-x","Test01"])
