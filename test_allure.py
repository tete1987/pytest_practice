#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/24 11:25 
# @Author : TETE
# @File : test_allure.py
import pytest

def test_success():
    assert True

def test_failure():
    assert False

def test_skip():
    pytest.skip('for a reason')

def test_broken():
    raise Exception('oops')