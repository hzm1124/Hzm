# [Case 4. 爱问财](https://www.iwencai.com/unifiedwap/result?w=%E4%BB%8A%E6%97%A5%E6%B6%A8%E5%81%9C&querytype=stock)

## 4.1. `JavaScript`进阶

- 每个对象的属性都会拥有一些可以自定义的配置项
  - `Object.getOwnPropertyDescriptor(对象, 属性名);`：获得属性的配置
  - `Object.defineProperty(对象, 属性名, {配置项});`：定义属性并自定义配置项

- 常用配置项
  - `configurable`：设置属性是否能被删除，是否能修改其配置项
  - `enumerable`：属性能否枚举，能通过`for in`循环或`Object.keys`遍历到的属性即为可枚举属性
  - `value`：属性值
  - `writable`：属性值是否能被修改
  - `get`和`set`：取属性和设置属性时执行对应的方法（`get`和`value`互相冲突，`set`和`writable`相冲突）
    - 获得属性的`get`方法：`对象.__lookupGetter__('属性名');`
    - 获得属性的`set`方法：`对象.__lookupSetter__('属性名');`

- `configurable`、`enumerable`、`writable`默认值
  - 通过普通赋值方式定义属性时，默认值为`true`
  - 通过`Object.defineProperty`定义属性时，默认值为`false`

## 4.2. 调用堆栈

- 对象的值会被当前作用域覆盖（引用类型、相同内存地址）
- 最简单的定位技巧：顺着调用堆栈不断向上寻找是否包含需要的加密参数，当某个堆栈下一层包含加密参数，上一层不包含加密参数，那么大概率就是在这一层生成的

## 4.3. 补环境

- 代码在浏览器环境可以正常运行 -> 我们需要让代码运行在`node`环境 -> 模拟浏览器环境
- 原则：浏览器有的我们也有，浏览器没有的我们也没有
- 技巧：某个东西不知道怎么来的 -> 与浏览器的相同代码段进行对比

## 4.4. 数字和字符串的相互转换

-  `'abcd'.charCodeAt(0)`获得对应索引字符串的数字表达形式（`python`：`ord('a')`）
- `String.fromCharCode(97)`，数字转字符串（`python`：`chr(97)` or `bytes([97]).decode()`）
 
## 4.5. 当怎么都找不到加密值时

1. 观察是用什么对象发送的请求
2. 如果值在请求体中，就查这个对象怎样设置请求体
3. `hook`对应的方法
  - 如：`XMLHttpRequest`对象通过`setRequestHeader`方法设置请求头，并且只允许设置不允许获取，则`hook`该方法
