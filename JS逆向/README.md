# TOC:

- [01. 摘要](./01.摘要)
- [02. 编码解码](./02.编码解码)
- [03. 加密解密](./03.加密解密)
- [04. 浏览器调试工具](./04.浏览器调试工具)
- [case01.有道翻译](./case01.有道翻译)
- [case02.网易云音乐](./case02.网易云音乐)
- [case03.易车](./case03.易车)

- - -

# 补充

## 1. `PyCharm`快捷键

- `ctrl` + `f`：搜索
- `ctrl` + `r`：搜索并替换
- `shift` + `F10`：运行代码
- `ctrl` + `F9`：调试代码
- `ctrl` + `/`：注释或解注释
- `ctrl` + `alt` + `l`：格式化选中代码
- `ctrl` + `d`：重复一行被选中代码
- `ctrl` + `p`：显示参数提示
- `ctrl` + `shift` + `-`：折叠所有代码
- `ctrl` + `shift` + `+`：展开所有代码
- 按住`alt`同时选中或插入光标
- 按下鼠标滚轮，多行同时插入光标

### 1.3.2. 调用堆栈
- 当怎么都找不到加密值时
  - 观察是用什么对象发送的请求
  - 如果值在请求体中，就查这个对象怎样设置请求体
  - `hook`对应的方法
    - 如：`XMLHttpRequest`对象通过`setRequestHeader`方法设置请求头，并且只允许设置不允许获取，则`hook`该方法

## 浏览器调试工具使用

    应用程序（Application）：
        在这个页面查看网站存储的信息，分为：
            Cookie（document.cookie）：
                Domain，属于哪个网站
                Expires / Max-Age，过期时间
                HttpOnly，如果值为真，则该 cookie 无法在 js 代码中获取
            本地存储（localStorage）：
                setItem 方法，设置键值对
                getItem 方法，取值
                removeItem 方法，删除键值对
            会话存储（sessionStorage）：
                同本地存储
        存储 -> 清除网站数据，可清空该网站存储的所有信息

## 在 py 调用 js 代码
        execjs 模块内部会使用到 process 对象，如果删除了 process 就会报错

    subprocess：
        import subprocess
        result = subprocess.run(['node', 'js文件路径'], capture_output=True, text=True, encoding='utf-8')
        result.stdout    # 获得js的打印输出信息
        运行原理：通过命令行调用 node
