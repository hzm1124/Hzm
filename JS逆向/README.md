# TOC:

- [01. 摘要](./01.摘要)
- [02. 编码解码](./02.编码解码)
- [03. 加密解密](./03.加密解密)
- [04. 浏览器调试工具](./04.浏览器调试工具)
- [05. `PyCharm`快捷键](./05.PyCharm快捷键)
- [case01. 有道翻译](./case01.有道翻译)
- [case02. 网易云音乐](./case02.网易云音乐)
- [case03. 易车](./case03.易车)
- [case04. 爱问财](./case04.爱问财)
- [case05. 中大网校](./case05.中大网校)

- - -


## 在 py 调用 js 代码
        execjs 模块内部会使用到 process 对象，如果删除了 process 就会报错

    subprocess：
        import subprocess
        result = subprocess.run(['node', 'js文件路径'], capture_output=True, text=True, encoding='utf-8')
        result.stdout    # 获得js的打印输出信息
        运行原理：通过命令行调用 node
