# -*- coding: utf-8 -*-
#@文件/File   : __init__.py
#@时间/Time   : 2022/12/21 04:56:49
#@作者/Author : 大灰狼 
#@邮件/Email  : dhltl@foxmail.com | ybsets@gmail.com


from Distbuild.packages_app_link import socket as call_socket
from Distbuild.packages_app_link import re_search as call_re_search
from Distbuild.packages_app_link import re_findall as call_re_findall
from Distbuild.packages_app_link import requests_get as call_requests_get
from Distbuild.packages_app_link import socks_SOCKS5 as call_socks_SOCKS5
from Distbuild.packages_app_link import socks_set_default_proxy as call_socks_set_default_proxy
from Distbuild.packages_app_link import socks_socksocket as call_socks_socksocket
from Distbuild.packages_app_link import json_load as call_json_load

from Distbuild.packages_app_link import PrivateSetPath as call_PrivateSetPath


class PrivateGetExRate:
    def __init__(self):
        # 获取配置文件路径
        self.var_GetJsonPath = call_PrivateSetPath().method_SetJsonPath('OpenAI-Config.json')

    def method_GetExRate(self, var_GetTokens:int):
        # 读取配置文件,读键'ChatGPT_proxy'的值, 再拆成ip和端口
        with open(self.var_GetJsonPath, 'r') as var_Temp:
            # 读取配置文件
            var_Data = call_json_load(var_Temp)
            # 读取键ChatGPT_proxy的值
            var_DataIPort = var_Data['ChatGPT']['ChatGPT_proxy']
            # 用正则拆分ip和端口 "socks5://127.0.0.1:10808"
            var_GetIPort = call_re_findall('([\\d.]+):([\\d]+)', var_DataIPort)[0]
        # 设置代理
        call_socks_set_default_proxy(call_socks_SOCKS5, var_GetIPort[0], int(var_GetIPort[1]))
        call_socket.socket = call_socks_socksocket

        # 设置爬取的url和header
        var_SetUrl = 'https://www.google.com/finance/quote/USD-CNY'
        var_SetHeaders = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                }

        # 获取内容
        var_GetHtmlText = call_requests_get(var_SetUrl, headers=var_SetHeaders).text
        # html_text = var_Res.text

        # 根据关键字获得汇率
        var_Reult = call_re_search(r'class=\"YMlKec fxKbKc\">(.*?)<\/div>', var_GetHtmlText)

        # 如果有内容, 输出获取的汇率, 1美元*汇率->人名币
        if var_Reult:
            var_GetExRate_USAToCNY = var_Reult.group(1)
            return self._method_CalculatePrice(var_GetExRate_USAToCNY, var_GetTokens)
        else:
            return False
    
    def _method_CalculatePrice(self, var_GetExRate:str, var_GetTokens:int):
        """
            - 根据汇率和上下文字符序列数, 计算成人名币价格
            - param: var_GetExRate>获取实时汇率, 如果未获取到实时汇率, 则会传入平均汇率6.6971
            - param: var_GetTokens>获取上下文字符序列数
            - return 上下文字符序列数消耗的人名币价格
                - 限1000个字符序列, 以此为基数
                - 每1000个字符序列消耗第四档位的价格:0.0002美元, 单价:0.0000002美元/个字符序列
                - 每1000个字符序列消耗第三档位的价格:0.0005美元, 单价:0.0000005美元/个字符序列
                - 每1000个字符序列消耗第二档位的价格:0.0020美元, 单价:0.000002美元/个字符序列
                - 每1000个字符序列消耗第一档位的价格:0.0200美元, 单价:0.00002美元/个字符序列
                - 目前程序固定第一档位
        """
        # 设定档位的美元单价
        var_PricePoints_A = 0.00002
        var_PricePoints_B = 0.000002
        var_PricePoints_C = 0.0000005
        var_PricePoints_D = 0.0000002

        # 每1000个字符序列消耗第一档位的价格:0.0200美元
        # 单价 0.00002美元/每个字符序列
        # 上下文字符序列数价格 = var_GetTokens * 0.00002
        # 计算上下文字符序列数消耗的美元价格, 根据实时汇率换算成人名币价格, 浮点数取小数点后六位
        var_Reult = (float(var_GetTokens) * var_PricePoints_A) * float(var_GetExRate)
        return round(var_Reult, 6)