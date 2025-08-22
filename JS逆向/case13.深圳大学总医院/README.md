# [Case 13. 深圳大学总医院](https://sugh.szu.edu.cn/html/index.html)

## 13. 补环境

- 原型检测
  - 看到取`__proto__`或`prototype`属性，大概率是进行原型检测

- 调用堆栈检测
  1. 实例化`Error`对象获得`stack`属性（应对：`hook Error`对象）
  2. 主动抛出异常，检测`cache`块中捕获的异常对象的`stack`属性
