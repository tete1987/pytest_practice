#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/23 9:17 
# @Author : TETE
# @File : conftest.py.py
import pytest
@pytest.fixture()
def login():
    print("这是个登录方法")


def pytest_configure(config):
  marker_list = ["case", "demo", "smoke"] # 标签名集合
  for markers in marker_list:
    config.addinivalue_line("markers", markers)
