# -*- coding: utf-8 -*-
#@文件/File   : AppCore.py
#@时间/Time   : 2022/12/15 02:55:51
#@作者/Author : 大灰狼 
#@邮件/Email  : dhltl@foxmail.com | ybsets@gmail.com

# 加入线程threading功能, 加入pyside6界面, 把三个变量改成json本地读取并可以手动设置
from .packages_app_link import json_load as call_json_load

from .packages_app_link import openai as call_openai
from .packages_app_link import transformers_GPT2TokenizerFast as call_transformers_GPT2TokenizerFast

from .packages_app_link import PrivateSetPath as call_PrivateSetPath
from .packages_app_link import PrivateGetExRate as call_PrivateGetExRate


class PrivateAppCore:
    def __init__(self):
        # 调用PrivateSetPath()这个类, 实现获取某些文件的路径
        var_LinkPrivateSetPath = call_PrivateSetPath()
        # 传递json文件名, 调取方法获取OpenAI-Config.json的文件路径
        var_GetJsonPath = var_LinkPrivateSetPath.method_SetJsonPath('OpenAI-Config.json')
        # 读文件内容
        with open(var_GetJsonPath, 'r', encoding='utf-8') as var_Temp:
            var_TempJsonData = call_json_load(var_Temp)
            # 配置OpenAI-API的组织ID和API密钥和代理
            call_openai.organization = var_TempJsonData['ChatGPT']['ChatGPT_organization']
            call_openai.api_key = var_TempJsonData['ChatGPT']['ChatGPT_apikey']
            # 代理这块就不做开关处理了
            call_openai.proxy = var_TempJsonData['ChatGPT']['ChatGPT_proxy']
        # 设定个空列表, 用于临时存储用户与ChatGPT每次对话产生的字符序列总数, 供method_GenerateResponse()使用
        self.var_SetTokensList = []
            
    def method_CheckTokenizer(self, var_GetMessage:str, var_ChickStatus:bool):
        """
            - 处理检查传入的字符数量
            - param: var_GetMessage>传入用户输入的文本
            - param: var_ChickStatus>True:会进入method_GenerateResponse, False:单纯的检查字符序列数量
            - return: 检查通过则进入 method_GenerateResponse , 不通过直接拒绝
        """
        var_Tokenizer = call_transformers_GPT2TokenizerFast.from_pretrained("gpt2")
        var_CheckLen = var_Tokenizer(var_GetMessage)['input_ids']
        # print('字符序列数: ',len(var_CheckLen))
        if var_ChickStatus == True:
            # print(var_GetMessage)
            if len(var_CheckLen) > 1000:
                # 限1000个字符序列
                return ['\u5b57\u6570\u8d85\u9650', len(var_CheckLen)]
            else:
                return self.method_GenerateResponse(var_GetMessage, len(var_CheckLen))
        elif var_ChickStatus == False:
            # print('检查机器人回复:', var_GetMessage, var_ChickStatus)
            return len(var_CheckLen)

    def method_GenerateResponse(self, var_GetMessage:str, var_GetTokens:int):#[ChatGPT回答:今天是星期五。 - 提问者:今天周几]今天周几
        """
            - text-davinci-003 text-ada-001 code-davinci-002
            - 传入值, 获取ChatGPT返回的数据
            - param: var_GetMessage>传入由method_CheckTokenizer方法过来的文本
            - param: var_GetTokens>传入字符序列数量(用户发送的, ChatGPT回复的)
            - return: ChatGPT返回的数据, 字符序列数量(用户发送的+ChatGPT回复的)
        """
        # 用户提问的内容, 计算出字符序列后存入列表
        self.var_SetTokensList.append(var_GetTokens)
        completions = call_openai.Completion.create(
            engine="text-davinci-003",# 选取的回答模型
            prompt=var_GetMessage,# 传入的文本值
            # suffix='',# 默认为空, 日后研究
            max_tokens=1024,# 不可超过engine参数中选取的模型,所限定的最大值
            # include_context=True,# 启用上下文关联
            temperature=0.5,# 范围0~1 | 0最准确
            top_p=1,# 采样答案的质量, 1为最高,即100%
            # instruction="Fix the spelling mistakes",
            n=1,# 默认值1, 不是很清楚具体作用, 但文档描述会影响到token配合, 也就是会实际影响账户余额
            stream=False,# 默认值False, 不是很清楚具体作用
            # logprobs='', # 默认空值 
            echo=False,
            # stop=[" Me:", " ChatGptAI:"],# 默认空值, 字符串或数组
            presence_penalty=0,# 默认值0, 范围-2.0~2.0
            frequency_penalty=0,# 默认值0, 范围-2.0~2.0
            # best_of=1,# 默认值1
            # logit_bias={"50256": -100}# 默认值空, 看不懂
            # user='DhlTest_1'# 寻思半天这玩意设了有什么用...
        )
        # 获取ChatGPT回复的内容, 这个内容是真正要拿去计算字符序列数的
        message = completions["choices"][0]["text"]
        # 将ChatGPT回复的内容, 通过method_CheckTokenizer()检查字符序列数
        self.var_SetTokensList.append(self.method_CheckTokenizer(message, False))
        # print(self.var_SetTokensList)
        # 求和列表元素
        var_GetListSum = sum(self.var_SetTokensList)
        # 清空掉列表
        self.var_SetTokensList = []
        # var_SetMemoryArchives = f"[ChatGPT回答:{message} - 提问者:{var_GetMessage}]"
        # 规整ChatGPT回复的内容, 去除一些多余的字符串
        var_NewMessage = message.replace('\n', '', 2).replace('，', '', 1)
        # 传入上下文总字符序列数, 计算人名币价格
        var_GetResult = call_PrivateGetExRate().method_GetExRate(var_GetListSum)
        return [var_NewMessage, var_GetResult]
        # =============================================
        # start_sequence = "\nChatGptAI:"
        # restart_sequence = "\nMe: "
        # # 设置通过代理访问,并且以数据流形式返回
        # import requests
        # import socks,socket
        # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10808) 
        # socket.socket = socks.socksocket
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Bearer {}'.format("sk-"),
        #     'OpenAI-Organization': 'org-'
        # }
        # response = requests.post('https://api.openai.com/v1/completions', headers=headers, json={
        # "model": "text-davinci-003",
        # "prompt": var_GetMessage,
        # "max_tokens": 1024,
        # "temperature": 0.5,
        # "presence_penalty": 0,
        # "frequency_penalty": 0,
        # "stream":True})
        # return response.text
        # =============================================

        # #判断回复时间
        # if completions["response_time"] < 55:
        #     return message
        # else:
        #     print("回复时间限制在50秒, 已暂停回复")