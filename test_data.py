#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/24 9:11 
# @Author : TETE
# @File : test_data.py
import pytest
import yaml

class TestData():
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a+b)

# class TestData():
#     @pytest.mark.parametrize(("a","b"),[(10,20),(10,30)])
#     def test_param(self,a,b):
#         print(a+b)
