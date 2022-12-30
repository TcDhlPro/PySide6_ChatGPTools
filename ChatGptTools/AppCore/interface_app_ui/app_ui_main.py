# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChatGPToolsflEAAU.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 600)
        MainWindow.setMinimumSize(QSize(560, 0))
        MainWindow.setMaximumSize(QSize(560, 1000))
        MainWindow.setToolTipDuration(0)
        MainWindow.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.tabWidget_1 = QTabWidget(self.centralwidget)
        self.tabWidget_1.setObjectName(u"tabWidget_1")
        self.tabWidget_1.setMinimumSize(QSize(530, 320))
        self.tabWidget_1.setMaximumSize(QSize(530, 320))
        self.tabWidget_1.setStyleSheet(u"")
        self.tab_ConfigurationOverview = QWidget()
        self.tab_ConfigurationOverview.setObjectName(u"tab_ConfigurationOverview")
        self.gridLayout_4 = QGridLayout(self.tab_ConfigurationOverview)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.groupBox_CostControl = QGroupBox(self.tab_ConfigurationOverview)
        self.groupBox_CostControl.setObjectName(u"groupBox_CostControl")
        self.groupBox_CostControl.setMinimumSize(QSize(500, 120))
        self.groupBox_CostControl.setMaximumSize(QSize(500, 120))
        self.groupBox_CostControl.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.groupBox_CostControl)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_CostControl)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(112, 21))
        self.label_4.setMaximumSize(QSize(112, 21))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_Payment_RealTime = QLabel(self.groupBox_CostControl)
        self.label_Payment_RealTime.setObjectName(u"label_Payment_RealTime")
        self.label_Payment_RealTime.setMinimumSize(QSize(111, 21))
        self.label_Payment_RealTime.setMaximumSize(QSize(111, 21))
        self.label_Payment_RealTime.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 700 9pt \"Microsoft YaHei UI\";\n"
"text-decoration: underline;")
        self.label_Payment_RealTime.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_Payment_RealTime, 0, 1, 1, 1)

        self.line = QFrame(self.groupBox_CostControl)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(3, 21))
        self.line.setMaximumSize(QSize(3, 21))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_CostControl)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 21))
        self.label_6.setMaximumSize(QSize(90, 21))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.label_6, 0, 3, 1, 1)

        self.comboBox_SlectEngine = QComboBox(self.groupBox_CostControl)
        self.comboBox_SlectEngine.addItem("")
        self.comboBox_SlectEngine.addItem("")
        self.comboBox_SlectEngine.addItem("")
        self.comboBox_SlectEngine.addItem("")
        self.comboBox_SlectEngine.setObjectName(u"comboBox_SlectEngine")
        self.comboBox_SlectEngine.setEnabled(False)
        self.comboBox_SlectEngine.setMinimumSize(QSize(140, 21))
        self.comboBox_SlectEngine.setMaximumSize(QSize(140, 21))
        self.comboBox_SlectEngine.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 700 9pt \"Microsoft YaHei UI\";")

        self.gridLayout_3.addWidget(self.comboBox_SlectEngine, 0, 4, 1, 1)

        self.line_2 = QFrame(self.groupBox_CostControl)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(480, 3))
        self.line_2.setMaximumSize(QSize(480, 3))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 5)

        self.label_7 = QLabel(self.groupBox_CostControl)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(191, 191, 191);")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 5)


        self.gridLayout_4.addWidget(self.groupBox_CostControl, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.groupBox_OpenAIConfig = QGroupBox(self.tab_ConfigurationOverview)
        self.groupBox_OpenAIConfig.setObjectName(u"groupBox_OpenAIConfig")
        self.groupBox_OpenAIConfig.setMinimumSize(QSize(500, 150))
        self.groupBox_OpenAIConfig.setMaximumSize(QSize(500, 16777215))
        self.groupBox_OpenAIConfig.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.groupBox_OpenAIConfig)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_OrganizationID = QLineEdit(self.groupBox_OpenAIConfig)
        self.lineEdit_OrganizationID.setObjectName(u"lineEdit_OrganizationID")
        self.lineEdit_OrganizationID.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_OrganizationID, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_OpenAIConfig)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.label_1 = QLabel(self.groupBox_OpenAIConfig)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.lineEdit_Socks = QLineEdit(self.groupBox_OpenAIConfig)
        self.lineEdit_Socks.setObjectName(u"lineEdit_Socks")
        self.lineEdit_Socks.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_Socks, 2, 2, 1, 1)

        self.lineEdit_APIKeys = QLineEdit(self.groupBox_OpenAIConfig)
        self.lineEdit_APIKeys.setObjectName(u"lineEdit_APIKeys")
        self.lineEdit_APIKeys.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_APIKeys, 0, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox_OpenAIConfig)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.pushButton_OpenAIConfigOK = QPushButton(self.groupBox_OpenAIConfig)
        self.pushButton_OpenAIConfigOK.setObjectName(u"pushButton_OpenAIConfigOK")
        self.pushButton_OpenAIConfigOK.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_OpenAIConfigOK, 1, 0, 1, 1)

        self.pushButton_OpenAIConfigReset = QPushButton(self.groupBox_OpenAIConfig)
        self.pushButton_OpenAIConfigReset.setObjectName(u"pushButton_OpenAIConfigReset")

        self.gridLayout_2.addWidget(self.pushButton_OpenAIConfigReset, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_OpenAIConfig, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 2, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 2, 2, 1, 1)

        self.tabWidget_1.addTab(self.tab_ConfigurationOverview, "")
        self.tab_AboutSelf = QWidget()
        self.tab_AboutSelf.setObjectName(u"tab_AboutSelf")
        self.gridLayout_5 = QGridLayout(self.tab_AboutSelf)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.tab_AboutSelf)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.tab_AboutSelf)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)

        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(163, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.label_8 = QLabel(self.tab_AboutSelf)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.tab_AboutSelf)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.MarkdownText)

        self.gridLayout_5.addWidget(self.label_9, 1, 1, 1, 2)

        self.horizontalSpacer_12 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 213, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 213, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.tabWidget_1.addTab(self.tab_AboutSelf, "")

        self.gridLayout_6.addWidget(self.tabWidget_1, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.plainTextEdit_ChatBody = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_ChatBody.setObjectName(u"plainTextEdit_ChatBody")
        self.plainTextEdit_ChatBody.setEnabled(True)
        self.plainTextEdit_ChatBody.setMinimumSize(QSize(530, 0))
        self.plainTextEdit_ChatBody.setMaximumSize(QSize(530, 1000))
        self.plainTextEdit_ChatBody.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.plainTextEdit_ChatBody.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit_ChatBody.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.plainTextEdit_ChatBody.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_ChatBody.setReadOnly(True)

        self.gridLayout_6.addWidget(self.plainTextEdit_ChatBody, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.widget_InputMsgBox = QWidget(self.centralwidget)
        self.widget_InputMsgBox.setObjectName(u"widget_InputMsgBox")
        self.widget_InputMsgBox.setMinimumSize(QSize(530, 25))
        self.widget_InputMsgBox.setMaximumSize(QSize(530, 25))
        self.widget_InputMsgBox.setInputMethodHints(Qt.ImhNone)
        self.pushButton_ForInputMsg = QPushButton(self.widget_InputMsgBox)
        self.pushButton_ForInputMsg.setObjectName(u"pushButton_ForInputMsg")
        self.pushButton_ForInputMsg.setGeometry(QRect(440, 0, 90, 25))
        self.pushButton_ForInputMsg.setMinimumSize(QSize(90, 25))
        self.pushButton_ForInputMsg.setMaximumSize(QSize(90, 25))
        self.lineEdit_InputMsg = QLineEdit(self.widget_InputMsgBox)
        self.lineEdit_InputMsg.setObjectName(u"lineEdit_InputMsg")
        self.lineEdit_InputMsg.setGeometry(QRect(0, 0, 435, 25))
        self.lineEdit_InputMsg.setMinimumSize(QSize(435, 25))
        self.label_LoadingProgress = QLabel(self.widget_InputMsgBox)
        self.label_LoadingProgress.setObjectName(u"label_LoadingProgress")
        self.label_LoadingProgress.setGeometry(QRect(0, 0, 530, 25))
        self.label_LoadingProgress.setMinimumSize(QSize(530, 25))
        self.label_LoadingProgress.setMaximumSize(QSize(530, 25))
        self.label_LoadingProgress.setAlignment(Qt.AlignCenter)
        self.label_LoadingProgress.raise_()
        self.pushButton_ForInputMsg.raise_()
        self.lineEdit_InputMsg.raise_()

        self.gridLayout_6.addWidget(self.widget_InputMsgBox, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_1.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"By: \u5927\u7070\u72fc", None))
        self.groupBox_CostControl.setTitle(QCoreApplication.translate("MainWindow", u"\u6210\u672c\u6d88\u8017/\u8ba1\u4ef7\u65b9\u5f0f(\u7b80\u5355\u7248|\u76ee\u524d\u529f\u80fd: \u8ba1\u7b97\u6bcf\u6b21\u63d0\u4ea4\u53ca\u56de\u590d\u540e\u6240\u6d88\u8017\u7684\u91d1\u989d, \u65e0\u5b58\u6863)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u8bf7\u6c42\u6d88\u8017\u91d1\u989d:", None))
        self.label_Payment_RealTime.setText(QCoreApplication.translate("MainWindow", u"0.000000\u5143", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53d8\u66f4\u8ba1\u4ef7\u65b9\u5f0f:", None))
        self.comboBox_SlectEngine.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u6863\u4f4d[\u4ef7\u683c\u6700\u9ad8]", None))
        self.comboBox_SlectEngine.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u6863\u4f4d[\u4ef7\u683c\u7a0d\u9ad8]", None))
        self.comboBox_SlectEngine.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u6863\u4f4d[\u4ef7\u683c\u4e2d\u7b49]", None))
        self.comboBox_SlectEngine.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u6863\u4f4d[\u4ef7\u683c\u6700\u4f4e]", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a\u7edf\u8ba1\u529f\u80fd: \u5f85\u5b9a", None))
        self.groupBox_OpenAIConfig.setTitle(QCoreApplication.translate("MainWindow", u"OpenAI\u914d\u7f6e", None))
        self.lineEdit_OrganizationID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u53c2\u8003-> xxx-xxxxxxxxxxxxxxxx | \u5fc5\u8981\u914d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Socks\u4ee3\u7406\u914d\u7f6e:", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"APIKeys:", None))
        self.lineEdit_Socks.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u53c2\u8003-> socks5://127.0.0.1:1080 | \u5fc5\u8981\u914d\u7f6e", None))
        self.lineEdit_APIKeys.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u53c2\u8003-> xx-xxxxxxxxxxxxxxxxxxxxxxxx | \u5fc5\u8981\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"OrganizationID:", None))
        self.pushButton_OpenAIConfigOK.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.pushButton_OpenAIConfigReset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u914d\u7f6e", None))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_ConfigurationOverview), QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6982\u89c8", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"V1.0.0.0(2022/12/29)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4ed3\u5e93\u5730\u5740:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"https://github.com/TcDhlPro/PySide6_ChatGPTools", None))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_AboutSelf), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_ChatBody.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.plainTextEdit_ChatBody.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_ForInputMsg.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
#if QT_CONFIG(shortcut)
        self.pushButton_ForInputMsg.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

