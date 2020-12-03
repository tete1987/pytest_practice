#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/20 17:07 
# @Author : TETE
# @File : test_pytest02.py
import pytest

def test_case1(login):
    print("test_case1")
    pass

def test_case2():
    print("test_case2")
    pass

@pytest.mark.case
def test_case3(login):
    print("test_case3")
    pass

if __name__ == "__main__":
    pytest.main()