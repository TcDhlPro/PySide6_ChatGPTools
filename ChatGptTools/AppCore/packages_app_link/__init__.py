# pip install openai==0.25.0
# pip install transformers==4.25.1
# pip install tensorflow==2.11.0
# pip install requests==2.28.1
# pip install PySide6==6.3.1

# //////弃用, 因openai模块中存在一些变量, 无法被引入修改, 应该是对象ID不一样了
# from openai import api_key as openai_api_key
# from openai import organization as openai_organization
# from openai import Completion as openai_Completion
# //////

# 内置库
from os import path as os_path
from os import environ as os_environ
from sys import argv as sys_argv
from sys import exit as sys_exit
from pathlib import Path as pathlib_Path
from json import load as json_load
from json import dump as json_dump
import socket
from re import search as re_search
from re import findall as re_findall
from socks import SOCKS5 as socks_SOCKS5
from socks import set_default_proxy as socks_set_default_proxy
from socks import socksocket as socks_socksocket
# 三方库
import openai
from requests import get as requests_get
from transformers import GPT2TokenizerFast as transformers_GPT2TokenizerFast
from PySide6.QtWidgets import QMainWindow as PySide6_QtWidgets_QMainWindow
from PySide6.QtWidgets import QApplication as PySide6_QtWidgets_QApplication
from PySide6.QtCore import QCoreApplication as PySide6_QtCore_QCoreApplication
from PySide6.QtWidgets import QMessageBox as PySide6_QtWidgets_QMessageBox
from PySide6.QtCore import QThread as PySide6_QtCore_QThread
from PySide6.QtCore import Signal as PySide6_QtCore_Signal
from PySide6.QtGui import QMovie as PySide6_QtGui_QMovie
from PySide6.QtCore import QTranslator as PySide6_QtCore_QTranslator
from PySide6.QtGui import QIcon as PySide6_QtGui_QIcon
from PySide6.QtCore import QSize as PySide6_QtCore_QSize
# from PySide6.QtCore import Qt as PySide6_QtCore_Qt
# 私模块
from AppCore.interface_app_ui import Ui_MainWindow as APP_MainWindow
from AppCore.function_app_core.function_set_path import PrivateSetPath
from AppCore.function_app_core.function_get_exrate import PrivateGetExRate