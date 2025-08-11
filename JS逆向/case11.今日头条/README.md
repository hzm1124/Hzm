# [Case 11. 今日头条]()

## 11.1. 补环境

- 检测`node`独有环境
  - `global`、`Buffer`、`process`使用`delete`删除
  - `module`、`exports`、__filename`__dirname`无法删除，只能赋值为`undefined`
  - `global[Symbol.toStringTag]`，模拟`window`对象时会导致问题，需要删除
- 绕过`Proxy`和报错
  - 使我们无法发觉环境检测
  - `typeof`未声明变量，不会报错
  - `'属性名' in 对象`，绕过`Proxy`
  - `Object`的一些方法，绕过`Proxy`









## 11.2. 风控

- 你的行为看起来不像一个正常使用浏览器访问网页的人 -> 拿不到数据
- 用户信息
  - 登陆状态下的`cookie` -> 无论你什么地方、什么浏览器、什么IP地址，只要你登陆这个账号，我就认识你
  - 未登陆状态下的`cookie` -> 换一个浏览器我就不认识你了
  - `IP`地址 -> 换个`WiFi`或者重启下网络`IP`就变了，我就不认识你了
- 需要认识
  - `cookie`指的不一定就是`cookie`，只要是一串能够识别你的字符（独一无二的）即可，放在什么地方都可以








