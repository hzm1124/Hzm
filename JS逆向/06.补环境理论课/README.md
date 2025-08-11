# 6. `PyCharm`快捷键

## 6.1. [`nvm`](https://github.com/coreybutler/nvm-windows/releases)管理`node`版本

- 目的：高版本`node`对于补环境来说非常不便（如必须保留`global`、`Buffer`对象），建议切换至17.9.1
- 安装指定版本`node`：`nvm install 版本`
- 查看已安装版本：`nvm list`
- 切换到指定版本：`nvm use 版本`

## 6.2. `Symbol`数据类型

- 我们实例化创建的`Symbol`用于表示一个独一无二的值
- 一些内置的`Symbol`用于一些特殊用途：
  - `Symbol.toStringTag`：调用对象的`toString`方法时使用此字符串
  - `node`和浏览器的对象存在一些内置`Symbol`属性
- `Symbol`作为属性名时，只能通过`Object.getOwnPropertySymbols`方法获得

## 6.3. `Object`常用静态方法

- `getOwnPropertyDescriptor(2arg)`：获得对象指定自身属性的配置项
- `getOwnPropertyDescriptors(1arg)`：获得对象自身所有属性的配置项
- `defineProperty(3arg)`：自定义属性的配置项
- `defineProperties(2arg)`：自定义多个属性的配置项
- `keys(1arg)`：获得对象自身所有可枚举属性
- `getOwnPropertyNames(1arg)`：同`keys`，但包含不可枚举属性
- `getOwnPropertySymbols(1arg)`：获得对象自身所有`Symbol`属性名
- `hasOwn(2arg)`：判断`参数2`是否是`参数1`自身拥有的属性
- `getPrototypeOf(1arg)`：获得对象的`__proto__`属性

## 6.4. `Object`原型常用方法

- `navigator.hasOwnProperty(1arg)`：判断参数是否是自身拥有属性
- `Navigator.prototype.isPrototypeOf(navigator)`：判断`Navigator.prototype`是否存在于`navigator`的原型链中，等价于`instanceof`关键字
- `__lookupGetter__`：获得`get`属性配置项
- `__lookupSetter__`：获得`set`属性配置项
- `toString`：转字符串形式
  - 对于原型方法：需要意识到所有对象使用`toString`时，使用的都是同一个`toString`，是`Object`原型上的，区别仅仅在于函数内的`this`指向不同，所以完全可以使用`call`方法调用进行平替





