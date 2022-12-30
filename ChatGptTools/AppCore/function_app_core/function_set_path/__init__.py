# -*- coding: utf-8 -*-
#@文件/File   : __init__.py
#@时间/Time   : 2022/12/17 08:05:49
#@作者/Author : 大灰狼 
#@邮件/Email  : dhltl@foxmail.com | ybsets@gmail.com

from AppCore.packages_app_link import os_path as call_os_path
from AppCore.packages_app_link import pathlib_Path as call_pathlib_Path


class PrivateSetPath:
    """
        1. 文件路径: 'ChatGptTools/AppCore/function_app_core/function_set_path/__init__.py'
    """
    def __init__(self):
        # 获取此脚本所在路径
        var_getAppPath = str(call_pathlib_Path(__file__).absolute().parent)
        # 根据获取的脚本路径, 返回至resource文件夹所在的目录
        self.var_getAppRoute = call_os_path.abspath(call_os_path.join(var_getAppPath, "../../.."))
    
    def method_SetJsonPath(self, var_getJsonName):
        """
            - 1. 功能: 设置Json文件的目录, 进行调用
            - 2. param: var_getJsonName>传入Json文件的文件名
            - 3. return: var_getJsonPath>返回Json文件的路径
        """
        # 设置文件读取路径 / 整合路径
        var_setJsonFolder = "resource/file_json/"
        var_getJsonRoutePath = call_os_path.join(self.var_getAppRoute, var_setJsonFolder, var_getJsonName)
        var_getJsonRoutePath = var_getJsonRoutePath.replace('\\', '/')
        return var_getJsonRoutePath
    
    def method_SetSvgPath(self, var_getSvgName):
        """
            - 1. 功能: 设置Svg文件的目录, 进行调用
            - 2. param: var_getSvgName>传入Svg文件的文件名
            - 3. return: var_getSvgRoutePath>返回Svg文件的路径
        """
        # 设置文件读取路径 / 整合路径
        var_setSvgFolder = "resource/file_svg/"
        var_getSVGRoutePath = call_os_path.join(self.var_getAppRoute, var_setSvgFolder, var_getSvgName)
        var_getSvgRoutePath = var_getSVGRoutePath.replace('\\', '/')
        return var_getSvgRoutePath

    def method_SetGifPath(self, var_getGifName):
        """
            - 1. 功能: 设置Gif文件的目录, 进行调用
            - 2. param: var_getGifName>传入Svg文件的文件名
            - 3. return: var_getGifRoutePath>返回Svg文件的路径
        """
        # 设置文件读取路径 / 整合路径
        var_setGifFolder = "resource/file_gif/"
        var_getGifRoutePath = call_os_path.join(self.var_getAppRoute, var_setGifFolder, var_getGifName)
        var_getGifRoutePath = var_getGifRoutePath.replace('\\', '/')
        return var_getGifRoutePath
    
    def method_SetLanguagePath(self, var_getLanguageName):
        """
            - 1. 功能: 设置Language文件的目录, 进行调用
            - 2. param: var_getLanguageName>传入翻译文件的文件名
            - 3. return: var_getLanguageRoutePath>返回翻译文件的路径
        """
        # 设置文件读取路径 / 整合路径
        var_setLanguageFolder = "resource/file_language/"
        var_getLanguageRoutePath = call_os_path.join(self.var_getAppRoute, var_setLanguageFolder, var_getLanguageName)
        var_getLanguageRoutePath = var_getLanguageRoutePath.replace('\\', '/')
        return var_getLanguageRoutePath