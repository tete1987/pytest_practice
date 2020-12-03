#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/25 9:25 
# @Author : TETE
# @File : test_attach.py
import pytest
import allure

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("这是一个html",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file(r"D:\Test\微信截图_20200911163252.png",name="这是一个图片",attachment_type=allure.attachment_type.PNG)