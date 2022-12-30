### ChatGPT工具助手
---

# 简介:
- 界面库用的是PySide6
- 需要准备个梯子
- 需要有个OpenAI的帐号
- OpenAI的API调用方式, 目前不具备让对话产生上下文关联, 是一次性对话
- 程序中做了简单的上下文关联, 只要对话不是特别离谱, 基本上使用起来还行, 你们也可以自己改个上下文关联的机制

  
# 准备工作及步骤:
- 在OpenAI后台申请一个 [API keys](https://beta.openai.com/account/api-keys)
- 在OpenAI后台查看组织ID [Organization ID](https://beta.openai.com/account/org-settings)
- 下载代码:
    ```shell 
    git@github.com:TcDhlPro/PySide6_ChatGPTools.git
    ```
- 进入目录:
    ```shell 
    cd PySide6_ChatGPTools
    ```
- 创建Python虚拟环境:
    ```shell 
    python -m venv VenvPathName
    ```
- 激活Python虚拟环境:
    ```shell 
    怎么激活自己百度下
    ```
- 在激活的虚拟环境中安装三方库:
    ```shell 
    pip install openai==0.25.0
    pip install transformers==4.25.1
    pip install tensorflow==2.11.0
    pip install requests==2.28.1
    pip install PySide6==6.3.1
    ```
- 进入目录:
    ```shell 
    cd PySide6_ChatGPTools/ChatGptTools
    ```
- 运行程序:
    ```shell
    python -m AppRun
    ```
    - 在这一步可能会遇到一个错误```Could not find the DLL(s) 'msvcp140_1.dll'```
    - 根据报错提示中的Url, 打开后再根据你的Python版本
    - 比如我是64位的, 我安装了```vc_redist.x64.exe```
- 程序截图参考:
    ![输入图片说明](https://agent-jsdelivr.gethub.tk/gh/TcDhlPro/blog_res/Other-images/ChatGPTools_Demo.png)
---

# 关于程序打包
- 我用的是Nuitka
- [程序下载-待定](https://www.google.com)
  - 不支持64位