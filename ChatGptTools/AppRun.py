# -*- coding: utf-8 -*-
#@文件/File   : AppRun.py
#@时间/Time   : 2022/12/14 17:28:40
#@作者/Author : 大灰狼 
#@邮件/Email  : dhltl@foxmail.com | ybsets@gmail.com

from AppCore.packages_app_link import sys_argv as call_sys_argv
from AppCore.packages_app_link import sys_exit as call_sys_exit
from AppCore.packages_app_link import json_load as call_json_load
from AppCore.packages_app_link import json_dump as call_json_dump
from AppCore.packages_app_link import os_environ as call_os_environ

from AppCore.packages_app_link import PySide6_QtWidgets_QMainWindow as call_PySide6_QtWidgets_QMainWindow
from AppCore.packages_app_link import PySide6_QtWidgets_QApplication as call_PySide6_QtWidgets_QApplication
from AppCore.packages_app_link import PySide6_QtCore_QCoreApplication as call_PySide6_QtCore_QCoreApplication
from AppCore.packages_app_link import PySide6_QtWidgets_QMessageBox as call_PySide6_QtWidgets_QMessageBox
from AppCore.packages_app_link import PySide6_QtCore_QThread as call_PySide6_QtCore_QThread
from AppCore.packages_app_link import PySide6_QtCore_Signal as call_PySide6_QtCore_Signal
from AppCore.packages_app_link import PySide6_QtGui_QMovie as call_PySide6_QtGui_QMovie
# from AppCore.packages_app_link import PySide6_QtCore_Qt as call_PySide6_QtCore_Qt
from AppCore.packages_app_link import PySide6_QtCore_QTranslator as call_PySide6_QtCore_QTranslator
from AppCore.packages_app_link import PySide6_QtGui_QIcon as call_PySide6_QtGui_QIcon
from AppCore.packages_app_link import PySide6_QtCore_QSize as call_PySide6_QtCore_QSize

from AppCore import PrivateAppCore as call_PrivateAppCore
from AppCore.packages_app_link import APP_MainWindow as call_APP_MainWindow
from AppCore.packages_app_link import PrivateSetPath as call_PrivateSetPath


class LinkAPPMainWindow(call_PySide6_QtWidgets_QMainWindow):
    def __init__(self):
        super().__init__()
        # 记录一下有些东西可以延迟加载, 尽量提高程序响应速度. 有些东西可以不一直占用内存, 减少内存占用
        # ====================================↓初始化相关↓====================================
        self.var_SetMsg = [
            # OpenAI配置信息不全
            'OpenAI\u914d\u7f6e\u4fe1\u606f\u4e0d\u5168',
            # 未输入有效提问
            '\u672a\u8f93\u5165\u6709\u6548\u63d0\u95ee',
            # 程序标题名称
            '\u0043\u0068\u0061\u0074\u0047\u0050\u0054\u5de5\u5177\u52a9\u624b\u002d\u0042\u0079\u003a\u5927\u7070\u72fc'
        ]
        # 传递配置文件的json文件名, 获取文件路径
        self.var_GetJsonPath = call_PrivateSetPath().method_SetJsonPath('OpenAI-Config.json')
        # 传递Gif文件名, 获取文件路径
        self.var_GetGifPath_ProgressLoading = call_PrivateSetPath().method_SetGifPath('ProgressLoading.gif')
        # 传递翻译文件名, 获取文件路径
        self.var_GetLanguagePath = call_PrivateSetPath().method_SetLanguagePath('qt_zh_CN.qm')
        # 传递ICON文件名, 获取文件路径
        self.var_GetWindowIconPath = call_PrivateSetPath().method_SetSvgPath('Icon.svg')

        # 程序运行时, 初始化一个提取聊天记录的字符串
        self.var_ExtractChatRecord = 'None'
        # ====================================↑初始化相关↑====================================

        # 实例化app_ui_main的Ui_MainWindow()
        self.var_GetAppMainWindow = call_APP_MainWindow()
        self.var_GetAppMainWindow.setupUi(self)
        self.method_SetUpUI()

    def method_SetUpUI(self):
        # ====================================↓界面相关↓====================================
        # 设置程序标题名称
        self.setWindowTitle(call_PySide6_QtCore_QCoreApplication.translate('MainWindow', self.var_SetMsg[2], None))

        # 设置程序图标
        var_WindowIcon = call_PySide6_QtGui_QIcon()
        var_WindowIcon.addFile(
            self.var_GetWindowIconPath,
            call_PySide6_QtCore_QSize(),
            var_WindowIcon.Normal,
            var_WindowIcon.Off
        )
        self.setWindowIcon(var_WindowIcon)
        self.setWindowOpacity(1.000000000000000)

        # 设置label_LoadingProgress进度组件初始隐藏
        self.var_GetAppMainWindow.label_LoadingProgress.hide()

        # 加载Gif图, 并关联到label_LoadingProgress进度组件上, gif模糊应该不是qt这块的问题
        #self.var_LinkMovieProgressLoading.start()# 播放gif
        # self.var_LinkMovieProgressLoading.setPaused(True)# 暂停播放
        self.var_LinkMovieProgressLoading = call_PySide6_QtGui_QMovie(self.var_GetGifPath_ProgressLoading)
        self.var_GetAppMainWindow.label_LoadingProgress.setMovie(self.var_LinkMovieProgressLoading)
        # ====================================↑界面相关↑====================================

        # ====================================↓检查相关↓====================================
        # 检查配置文件
        with open(self.var_GetJsonPath, 'r') as var_temp:
            var_data = call_json_load(var_temp)
            var_Get_A = var_data['ChatGPT']['ChatGPT_organization']
            var_Get_B = var_data['ChatGPT']['ChatGPT_apikey']
            var_Get_C = var_data['ChatGPT']['ChatGPT_proxy']
            if var_Get_A and var_Get_B and var_Get_C != None:
                self.var_GetAppMainWindow.lineEdit_OrganizationID.setText(var_Get_A)
                self.var_GetAppMainWindow.lineEdit_APIKeys.setText(var_Get_B)
                self.var_GetAppMainWindow.lineEdit_Socks.setText(var_Get_C)
            else:
                # 无所谓, 反正弹窗提示会出手!
                pass
        # ====================================↑检查相关↑====================================

        # 初始化动态SVG/静态SVG, 日后优化, QT好像无法实现-显示动态SVG

        # 设置关键词语法高亮, 日后优化

        # 记录下其他待优化, 某些方法调用通过线程, 尽量不堵塞主程序

        # ====================================↓功能相关↓====================================
        # 连接用户提交按钮的点击信号至method_ClickEvent_ForInputMsg()方法槽
        self.var_GetAppMainWindow.pushButton_ForInputMsg.clicked.connect(self.method_ClickEvent_ForInputMsg)

        # 连接保存配置按钮的点击信号至method_ClickEvent_OpenAIConfigOK()方法槽
        self.var_GetAppMainWindow.pushButton_OpenAIConfigOK.clicked.connect(self.method_ClickEvent_OpenAIConfigOK)

        # 连接重置配置按钮的点击信号至method_ClickEvent_OpenAIConfigReset()方法槽
        self.var_GetAppMainWindow.pushButton_OpenAIConfigReset.clicked.connect(self.method_ClickEvent_OpenAIConfigReset)
        # ====================================↑功能相关↑====================================

    def method_ClickEvent_ForInputMsg(self):
        """
            - 提交按钮的检查事件
                - 用户点击提交按钮后, 检查OpenAI配置中的三个必填项和提问项是否为空值
        """
        if len(self.var_GetAppMainWindow.lineEdit_APIKeys.text()) == 0:
            # OpenAI配置信息APIKeys不全的弹窗提示
            self.var_GetAppMainWindow.lineEdit_InputMsg.clear()
            call_PySide6_QtWidgets_QMessageBox.information(self, "Error", self.var_SetMsg[0], call_PySide6_QtWidgets_QMessageBox.Ok)
        elif len(self.var_GetAppMainWindow.lineEdit_OrganizationID.text()) == 0:
            # OpenAI配置信息OrganizationID不全的弹窗提示
            self.var_GetAppMainWindow.lineEdit_InputMsg.clear()
            call_PySide6_QtWidgets_QMessageBox.information(self, "Error", self.var_SetMsg[0], call_PySide6_QtWidgets_QMessageBox.Ok)
        elif len(self.var_GetAppMainWindow.lineEdit_Socks.text()) == 0:
            # OpenAI配置信息Socks不全的弹窗提示
            self.var_GetAppMainWindow.lineEdit_InputMsg.clear()
            call_PySide6_QtWidgets_QMessageBox.information(self, "Error", self.var_SetMsg[0], call_PySide6_QtWidgets_QMessageBox.Ok)
        elif len(self.var_GetAppMainWindow.lineEdit_InputMsg.text()) == 0:
            # lineEdit_InputMsg组件内容为空的弹窗提示
            call_PySide6_QtWidgets_QMessageBox.information(self, "Error", self.var_SetMsg[1], call_PySide6_QtWidgets_QMessageBox.Ok)
            # 检查通过, 放行
        else:
            # 进入检查聊天记录的方法
            var_GetResult = self.method_CheckChatRecord()
            if var_GetResult == 'Clear':
                # 获取lineEdit_InputMsg输入框内容
                var_GetMessage = self.var_GetAppMainWindow.lineEdit_InputMsg.text()
                # 清空lineEdit_InputMsg输入框内容
                self.var_GetAppMainWindow.lineEdit_InputMsg.clear()
                # 禁用lineEdit_InputMsg和pushButton_ForInputMsg和pushButton_OpenAIConfigReset三个组件, 等ChatGPT有回复后, 再恢复
                self.method_ClickEvent_PushButtonForInputMsg(False)
                # 将用户提交的内容, 进行显示输出
                self.var_GetAppMainWindow.plainTextEdit_ChatBody.appendPlainText(u'[\u6211]\n    ' + var_GetMessage + '\n')
                # 将用户提交的内容, 存入列表
                self.var_ChatRecord.append(var_GetMessage)
                # 将内容给到method_QThreadAlloc()方法
                self.method_QThreadAlloc(var_GetMessage, 10000)
                # self.var_GetAppMainWindow.textEdit_ChatBody.setPlainText('\u6211:\n    '+'你好!\n'+'------\n')
            else:
                # 获取lineEdit_InputMsg输入框内容
                var_GetMessage = self.var_GetAppMainWindow.lineEdit_InputMsg.text()
                # 清空lineEdit_InputMsg输入框内容
                self.var_GetAppMainWindow.lineEdit_InputMsg.clear()
                # 禁用lineEdit_InputMsg和pushButton_ForInputMsg和pushButton_OpenAIConfigReset三个组件, 等ChatGPT有回复后, 再恢复
                self.method_ClickEvent_PushButtonForInputMsg(False)
                # 将用户提交的内容, 进行显示输出
                self.var_GetAppMainWindow.plainTextEdit_ChatBody.appendPlainText(u'[\u6211]\n    ' + var_GetMessage + '\n')
                # 将用户提交的内容, 存入列表
                self.var_ChatRecord.append(var_GetMessage)
                # 设置新的提交内容
                var_NewMessage = var_GetResult + var_GetMessage + '\n'
                # 将内容给到method_QThreadAlloc()方法
                self.method_QThreadAlloc(var_NewMessage, 10000)
    
    def method_CheckChatRecord(self):
        """
            - 在用户按下pushButton_ForInputMsg按钮后, 程序都会来这里检查下, 是否有之前的聊天记录
            - 如果没有, 正常走
            - 如果有, 带着之前记录一起走
            - 作用是让用户与ChatGPT的对话, 产生上下文关联, 不是死板的一次性对话
            - return>看下方的条件表达吧
        """
        # 每次进入都会初始化这个列表, 用来存储聊天记录, 只会存储新对话的上一次内容
        self.var_ChatRecord = []
        # print('聊天记录字符串检查:',self.var_ExtractChatRecord)
        # 检查提取聊天记录的字符串
        if self.var_ExtractChatRecord != 'None':
            # var_TempExtractChatRecord = self.var_ExtractChatRecord
            # self.var_ExtractChatRecord = 'None'
            return self.var_ExtractChatRecord
        else:
            return 'Clear'

    def method_ClickEvent_OpenAIConfigOK(self):
        """
            - 保存配置按钮
        """
        # 读
        with open(self.var_GetJsonPath, 'r') as var_Temp_1:
            # 加载配置文件
            var_Data = call_json_load(var_Temp_1)
            # 读取OpenAI配置的三项输入框内容
            var_Data['ChatGPT']['ChatGPT_organization'] = self.var_GetAppMainWindow.lineEdit_OrganizationID.text()
            var_Data['ChatGPT']['ChatGPT_apikey'] = self.var_GetAppMainWindow.lineEdit_APIKeys.text()
            var_Data['ChatGPT']['ChatGPT_proxy'] = self.var_GetAppMainWindow.lineEdit_Socks.text()

        # 写
        with open(self.var_GetJsonPath, 'w') as var_temp_2:
            call_json_dump(var_Data, var_temp_2, indent=4)

        # 写完后禁用四项内容(一个按钮,三个输入框)
        self.var_GetAppMainWindow.lineEdit_APIKeys.setEnabled(False)
        self.var_GetAppMainWindow.lineEdit_OrganizationID.setEnabled(False)
        self.var_GetAppMainWindow.lineEdit_Socks.setEnabled(False)
        self.var_GetAppMainWindow.pushButton_OpenAIConfigOK.setEnabled(False)

    def method_ClickEvent_OpenAIConfigReset(self):
        """
            - 重置配置按钮
        """
        # 解开禁用的四项内容(一个按钮,三个输入框)
        self.var_GetAppMainWindow.lineEdit_APIKeys.setEnabled(True)
        self.var_GetAppMainWindow.lineEdit_OrganizationID.setEnabled(True)
        self.var_GetAppMainWindow.lineEdit_Socks.setEnabled(True)
        self.var_GetAppMainWindow.pushButton_OpenAIConfigOK.setEnabled(True)
    
    def method_ClickEvent_PushButtonForInputMsg(self, var_GetStatus:bool):
        """
            - 在用户按下pushButton_ForInputMsg按钮点击后, 处理相关组件的禁用和恢复
            - param: var_GetStatus>接收布尔值, True为恢复, Flase为禁用
        """
        if var_GetStatus == True:
            self.var_GetAppMainWindow.label_LoadingProgress.hide()
            self.var_LinkMovieProgressLoading.setPaused(True)
            self.var_GetAppMainWindow.lineEdit_InputMsg.show()
            self.var_GetAppMainWindow.pushButton_ForInputMsg.show()
            self.var_GetAppMainWindow.lineEdit_InputMsg.setEnabled(True)
            self.var_GetAppMainWindow.pushButton_ForInputMsg.setEnabled(True)
            self.var_GetAppMainWindow.pushButton_OpenAIConfigReset.setEnabled(True)
        elif var_GetStatus == False:
            self.var_GetAppMainWindow.lineEdit_InputMsg.setEnabled(False)
            self.var_GetAppMainWindow.pushButton_ForInputMsg.setEnabled(False)
            self.var_GetAppMainWindow.pushButton_OpenAIConfigReset.setEnabled(False)
            self.var_GetAppMainWindow.lineEdit_InputMsg.hide()
            self.var_GetAppMainWindow.pushButton_ForInputMsg.hide()
            self.var_GetAppMainWindow.label_LoadingProgress.show()
            self.var_LinkMovieProgressLoading.start()

    def method_QThreadAlloc(self, var_GetContent:str, var_GetIDCode:int):
        """
            - 线程分配处理, 根据传入的指令执行相应的逻辑代码
        """
        if var_GetIDCode == 10000:
            # 启动线程, 进入[self.var_GetIDCode == 10000] | 初始化线程和启动线程要用成员变量, 不能用局部变量, 否则线程失败
            self.var_QThreadA = IntoQThread()
            self.var_QThreadA.function_getIDCode(var_GetContent, 10000)
            self.var_QThreadA.start()
            self.var_QThreadA.var_updateSignal.connect(self.method_GetQThreadResult)# 接收信号后, 带着结果进入此方法

    def method_GetQThreadResult(self, var_GetQThreadResult:list):
        """
            - 接收线程返回的 ChatGPT回复的内容, 并进行相应处理
        """
        # 将ChatGPT回复的内容, 进行显示输出
        self.var_GetAppMainWindow.plainTextEdit_ChatBody.appendPlainText('[ChatGPT]\n    ' + var_GetQThreadResult[0] + '\n----------\n')
        # 将 因上下文字符序列数 消耗的价格, 进行显示输出
        self.var_GetAppMainWindow.label_Payment_RealTime.setText(str(var_GetQThreadResult[1]) + '元')
        # 将ChatGPT回复的内容, 存入列表
        self.var_ChatRecord.append(var_GetQThreadResult[0])
        # 再把列表中的元素提取出来, 组成提取聊天记录的字符串, 最终格式:[ 提问者:今天周几 - ChatGPT回答:今天是星期五。]新的问题\n
        self.var_ExtractChatRecord = f'[\u63d0\u95ee\u8005:{self.var_ChatRecord[0]} - ChatGPT\u56de\u7b54:{self.var_ChatRecord[1]}]'
        # 恢复lineEdit_InputMsg和pushButton_ForInputMsg和pushButton_OpenAIConfigReset三个组件
        self.method_ClickEvent_PushButtonForInputMsg(True)


class IntoQThread(call_PySide6_QtCore_QThread):
    """
        1.功能: QThread多线程入口
    """
    # 设置值变化信号
    var_updateSignal = call_PySide6_QtCore_Signal(list)
    def __init__(self):
        super(IntoQThread, self).__init__()
    
    def function_getIDCode(self, var_GetPushMsg:str, var_GetIDCode:int):
        """
            - 根据指令启动线程
            - 10000-19999
                - 10000: 将用户输入的内容,交给call_PrivateAppCore().method_CheckTokenizer进行处理
                - 10001: 
            - 20000-29999
                - 20000: 
            - 30000-39999
                - 30000:
        """
        self.var_GetPushMsg = var_GetPushMsg
        self.var_GetIDCode = var_GetIDCode

    def run(self):
        if self.var_GetIDCode == 10000:
            # 获取ChatGPT回复的结果和上下文消耗的价格
            var_GetResultA = call_PrivateAppCore().method_CheckTokenizer(self.var_GetPushMsg, True)# 数据返回
            self.var_updateSignal.emit(var_GetResultA)# 发送数据, 
            self.quit()
        # elif self.var_getIDCode == 10001:

# AppCore测试
if __name__ == "__main__":
    # 如果要适配清晰度和软件大小的自适应, 其实不应该用下方这一句话, 要搭配win32库去获取屏幕分辨率及屏幕xy轴的长度, 再去计
    # 算DPI缩放倍数, 根据缩放倍数设定DPI和设定合适的软件大小, 因为相同的屏幕缩放率, 可能分辨率不同, 可能DPI缩放倍数不同
    # call_os_environ["QT_FONT_DPI"] = "150"
    # call_PySide6_QtWidgets_QApplication.setAttribute(call_PySide6_QtCore_Qt.AA_EnableHighDpiScaling)不采用
    # call_PySide6_QtWidgets_QApplication.setAttribute(call_PySide6_QtCore_Qt.AA_high)不采用
    var_App = call_PySide6_QtWidgets_QApplication(call_sys_argv)
    var_AppWindow = LinkAPPMainWindow()
    
    # 加载翻译文件, 本想解决右键菜单中文的问题, 没啥效果
    var_translator = call_PySide6_QtCore_QTranslator()
    var_translator.load(var_AppWindow.var_GetLanguagePath)
    var_App.installTranslator(var_translator)

    var_AppWindow.show()
    call_sys_exit(var_App.exec())