# [Case 12. 中华人民共和国海关总署](http://www.customs.gov.cn/customs/302249/302266/08654b53-1.html)

## 12.1. 补环境

- 函数检测点
  - `toString`、格式化、参数个数、函数名称、`arguments`
  - `"use strict";`

## 12.2. 浏览器联调工具

- 安装：`npm install -g node-inspect`
- 启动：`node-inspect 文件路径`

## 12.3. 在`Python`调用`JavaScript`代码

- ```JavaScript
  import subprocess
  result = subprocess.run(['node', 'js文件路径'],
                          capture_output=True,
                          text=True,
                          encoding='utf-8')
  result.stdout
  ```


















