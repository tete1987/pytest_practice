#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/11/24 10:25 
# @Author : TETE
# @File : test_cs.py
import pytest
import yaml
class TestCs():
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_cs(self,env):
        if "test_case" in env:
            print("这是测试环境")
            print("测试环境的IP地址是：",env["test_case"])
        if "dev" in env:
            print("这是正式环境")