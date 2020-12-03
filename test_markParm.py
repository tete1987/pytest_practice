#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/23 9:58 
# @Author : TETE
# @File : test_markParm.py
import pytest
import sys

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("5*8",40),("8+3",89)])
def test_eval(test_input,expected):

    assert eval(test_input) == expected